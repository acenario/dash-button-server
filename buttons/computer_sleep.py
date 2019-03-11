import os
import time
import subprocess
from app import manager
from buttons.base.base_button import BaseButton

class ComputerSleepButton(BaseButton):    
    def __init__(self):
        super(ComputerSleepButton, self).__init__()
        self.name = "computer_sleep"
    
    def action(self, event):
        self.say("hello")

t = ComputerSleepButton()
t.start()