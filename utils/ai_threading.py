import threading

class AiThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self,group=None, target=None, name=None, cleanup=None, args=(), kwargs={}):
        if name:
            args += (name,)
        super(AiThread, self).__init__(group, target, name, args, kwargs)
        self._stop = threading.Event()
        self.cleanup = cleanup

    def stop(self):
        self._stop.set()
        if self.cleanup:
            self.cleanup()

    def stopped(self):
        return self._stop.isSet()

    def start_thread(self):
        self.daemon = True
        self.start()

        return self