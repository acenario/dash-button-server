from app import manager
from abc import ABC, abstractmethod
from utils.ai_threading import AiThread
from utils.custom_decorators import abstract_class_attributes

# @abstract_class_attributes("name", "main_thread")
class BaseThread(ABC):
    def __init__(self):
        self.name = "thread_name"
        self.main_thread = False

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls().name is NotImplemented:
            # Choose your favorite exception.
            raise NotImplementedError('You forgot to define {name}')
        if cls().main_thread is NotImplemented:
            # Choose your favorite exception.
            raise NotImplementedError('You forgot to define {main_thread}')

    @abstractmethod
    def blocking(self):
        pass

    @abstractmethod
    def main(self, thread_name):
        if self.main_thread:
            thread = manager.main_threads[thread_name]
        else:
            thread = manager.background_threads[thread_name]
        while not thread.stopped():
            self.blocking()

    @abstractmethod
    def start(self):
        thread = AiThread(target=self.main, name=self.name, cleanup=self.stop)
        if self.main_thread:
            manager.main_threads[self.name] = thread
        else:
            manager.background_threads[self.name] = thread
        thread.start_thread()

    @abstractmethod
    def stop(self):
        pass