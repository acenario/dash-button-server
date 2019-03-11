import time
import queue 
from app import manager
from copy import deepcopy
from db.models.button import Button
from threads.base.base_thread import BaseThread
from scapy.all import *

class ButtonListenerThread(BaseThread):    
    def __init__(self):
        self.name = "blocking_main_queue"
        self.main_thread = True
        self.should_stop = False
        self.cooldown = 5

    def detect_button(self, pkt):
        if pkt.haslayer(DHCP) and pkt[Ether].src in manager.cache["buttons"]:
            mac = pkt[Ether].src
            thread_name = manager.cache["buttons"][mac]["name"]
            btn_id = manager.cache["buttons"][mac]["btn_id"]
            if thread_name in manager.background_threads:
                if (Button.should_register_push(btn_id, self.cooldown)):
                    thread = manager.background_threads[thread_name]
                    thread.queue.put(mac)

    def blocking(self):
        sniff(prn=self.detect_button, filter="(udp and (port 67 or 68))", store=0, stop_filter=self.cleanup)

    def main(self, thread_name):
        super().main(thread_name)

    def start(self):
        super().start()

    def cleanup(self, pkt):
        if self.should_stop:
            return True
        return False

    def stop(self):
        self.should_stop = True

t = ButtonListenerThread()
t.start()