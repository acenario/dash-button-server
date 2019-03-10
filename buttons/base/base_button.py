import queue 
from app import manager
from abc import ABC, abstractmethod
from utils.ai_threading import AiThread
from utils.custom_decorators import abstract_class_attributes

class BaseButton:
    def __init__(self):
        self.name = "button_name"
        self.event_queue = queue.Queue()

    def action(self, event):
        raise NotImplementedError('You forgot to define an action.')

    def blocking(self):
        event = self.event_queue.get()
        self.action(event)

    def main(self, thread_name):
        thread = manager.background_threads[thread_name]
        while not thread.stopped():
            self.blocking()

    def start(self):
        thread = AiThread(target=self.main, name=self.name, cleanup=self.stop)
        thread.queue = self.event_queue
        manager.background_threads[self.name] = thread
        thread.start_thread()

    def stop(self):
        self.event_queue = queue.Queue()