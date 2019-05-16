import os
import time
import queue 
import subprocess
from app import manager, app
from abc import ABC, abstractmethod
from utils.ai_threading import AiThread
from utils.custom_decorators import abstract_class_attributes

class BaseButton:
    def __init__(self):
        self.name = "button_name"
        self.event_queue = queue.Queue()
    
    def say(self, text):
        f = open(os.devnull, 'w')
        subprocess.Popen(["say",
                        text, 
                        ], stdout=f)

    def play(self, sound_name):
        f = open(os.devnull, 'w')
        resource_path = os.path.join(app.root_path, 'static', 'sounds', sound_name)
        subprocess.Popen(["afplay",
                        resource_path, 
                        ], stdout=f)

    def sshcmd(self, host, command, user=None, stdin=None, check=False):
        ''' Runs ssh command via subprocess.  Assuming .ssh/config is configured.

        Args:
            host: target host to send the command to
            command: command to run on the host
            user: (optional) user to use to login to host
            stdin: (optional) override sys.stdin
            check: (optional) pass to *subprocess.run*; if set, checks return code
                and raises subprocess.CalledProcessError, if none-zero result

        Returns:
            subprocess.CompletedProcess object
        '''

        where = "%s" % host if user is None else "%s@%s" %(user, host)
        result = subprocess.run(["ssh", where, command],
                            shell=False,
                            stdin=stdin,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            check=check)
        return result

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