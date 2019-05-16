import os
import time
import asyncio
import subprocess
from pyatv import helpers
from app import manager, app
from buttons.base.base_button import BaseButton

class AppleTVButton(BaseButton):    
    def __init__(self):
        super(AppleTVButton, self).__init__()
        self.name = "apple_tv_button_name"
    
    def send_appletv_commands(self, cmds):
        print("step 2")
        thread = manager.background_threads[self.name]
        asyncio.set_event_loop(thread.loop)
        for cmd in cmds:
            print(cmd)
            @asyncio.coroutine
            def make_cmd(atv):
                for instruction in cmd:
                    print(instruction)
                    x = 0
                    instruc_type = instruction[0]
                    qty = instruction[1]
                    while x < qty:
                        func = None
                        if instruc_type is "menu":
                            func =  atv.remote_control.top_menu
                        elif instruc_type is "up":
                            func =  atv.remote_control.up
                        elif instruc_type is "down":
                            func =  atv.remote_control.down
                        elif instruc_type is "left":
                            func =  atv.remote_control.left
                        elif instruc_type is "right":
                            func =  atv.remote_control.right 
                        elif instruc_type is "select":
                            func =  atv.remote_control.select             
                        if func:
                            yield from func()
                            print("here 1")
                        else:
                            print("here 2")
                        x+=1
            helpers.auto_connect(make_cmd)