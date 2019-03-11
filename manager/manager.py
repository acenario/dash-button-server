import queue 
from utils.colors import ConsoleColors

class AppManager(object):
    """ App Manager Class
    """
    def __init__(self):
        """ Constructor
        Set all the default vars
        """

        self.lang_code = 'en-US' #Will add langauge support in future
        self.main_threads = {}
        self.background_threads = {}
        self.main_queue = queue.Queue()
        self.error_queue = queue.Queue()
        self.cache = {}

        #Eventually translate AppManager into simpler manager with AppStack
        #Replicate ABC Stack

        """
        Future Stack Concept for Ai:
        (up)
        Socket/App Layer --> Communicating to plugins / sending data to external devices
        (up)
        Network Layer --> Inspecting packet 
        (up)
        Datalink --> Figuring out if message belonged to system
        (up)
        Physical --> Listening Layer / Convert to text if necessary
        (up)
        """

        #Physical --> Listening Layer

    def test(self):
        pass

    def load_button_modules(self):
        from buttons.base.all_buttons import LoadModules
        LoadModules()
    
    def load_thread_modules(self):
        from threads.base.all_threads import LoadModules
        LoadModules()

    def start(self):
        self.load_button_modules()
        self.load_thread_modules()
            
    def cleanup(self):
        for thread in self.main_threads:
            self.main_threads[thread].stop()
        
        for thread in self.background_threads:
            self.background_threads[thread].stop()

    def stop(self):
        """Tell process to tear down the manager.
        Stop the background manager process.
        """
        self.cleanup()

    def print_str(self, object,str_type):
        print(object)

    def log(self, object, str_type=ConsoleColors.get_info_string):
        self.print_str("[-] " + str(object), str_type)

    def warning(self, object):
        self.print_str("[!] " + str(object), ConsoleColors.get_fail_string)

    def success(self, object):
        self.print_str("[+] " + str(object), ConsoleColors.get_ok_string)

    def start_thread(self, bg_function, args=(), main_thread=False, name=None):        
        pass

    def blocking_error_reporting(self,thread_name):
        pass