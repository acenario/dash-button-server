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
        sleep_cmd = app.config["SLEEP_CMD"]
        #out = self.sshcmd(computer_name, command_2, user=user_name, check=False).stdout.decode()
        self.sshcmd(computer_name, sleep_cmd, user=user_name, check=False)

t = ComputerSleepButton()
t.start()