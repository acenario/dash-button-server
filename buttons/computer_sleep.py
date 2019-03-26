import os
import time
import subprocess
from app import manager, app
from buttons.base.base_button import BaseButton

class ComputerSleepButton(BaseButton):    
    def __init__(self):
        super(ComputerSleepButton, self).__init__()
        self.name = "computer_sleep"
    
    def action(self, event):
        # self.say("hello")
        computer_name = app.config["COMPUTER_NAME"]
        user_name = app.config["USER_NAME"]
        command_1 = app.config["CMD_1"]
        command_2 = app.config["CMD_2"]
        host_id = "{}@{}".format(user_name,computer_name)
        subprocess.call([command_1, host_id, "'{}'".format(command_2)], shell=False)

t = ComputerSleepButton()
t.start()