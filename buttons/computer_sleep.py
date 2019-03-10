import time
from app import manager
from buttons.base.base_button import BaseButton

class ComputerSleepButton(BaseButton):    
    def __init__(self):
        super(ComputerSleepButton, self).__init__()
        self.name = "computer_sleep"
        

    def action(self, event):
        print("Pushed the button! Text Entered: {}".format(event))

t = ComputerSleepButton()
t.start()