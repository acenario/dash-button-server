import time
import queue 
import requests
from copy import deepcopy
from utils.networking import Networking
from sudo_needed.base.base_thread import BaseThread
from network_app import manager
from scapy.all import *

class ButtonListenerThread(BaseThread):    
    def __init__(self):
        self.name = "blocking_main_queue"
        self.main_thread = True
        self.should_stop = False
        self.cooldown = 5

    def fetch_buttons(self):
        ip = Networking.get_ip_address()
        addr = "http://{}:{}/buttons".format(ip,"5000")
        r = requests.get(addr)
        if r.status_code == 200:
            buttons_dict = r.json()
            manager.cache["buttons"] = buttons_dict
            return buttons_dict
        print(r.text)
        return None

    def send_button_push(self, thread_name, mac, btn_id, cooldown=None):
        if not cooldown:
            cooldown = self.cooldown
        ip = Networking.get_ip_address()
        addr = "http://{}:{}/push".format(ip,"5000")
        button_dict = {"push": {
                            "thread_name": thread_name,
                            "mac": mac,
                            "btn_id": btn_id,
                            "cooldown": cooldown
                            }
                        }
        r = requests.post(addr, json=button_dict)
        if r.status_code is not 200:
            print(r.text)
        return r

    def detect_button(self, pkt):
        self.fetch_buttons()
        if pkt.haslayer(DHCP) and pkt[Ether].src in manager.cache["buttons"]: #STAY SAME
            mac = pkt[Ether].src
            thread_name = manager.cache["buttons"][mac]["name"] #STAY SAME
            btn_id = manager.cache["buttons"][mac]["btn_id"] #STAY SAME
            self.send_button_push(thread_name, mac, btn_id)

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