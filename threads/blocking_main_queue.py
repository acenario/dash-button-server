import time
import queue 
from app import manager
from threads.base.base_thread import BaseThread

class MainQueueThread(BaseThread):    
    def __init__(self):
        self.name = "blocking_main_queue"
        self.main_thread = True

    def routing(self, action):
        pass

    def blocking(self):
        action = manager.main_queue.get()
        self.routing(action)

    def main(self, thread_name):
        super().main(thread_name)

    def start(self):
        super().start()

    def stop(self):
        manager.main_queue = queue.Queue()

t = MainQueueThread()
t.start()