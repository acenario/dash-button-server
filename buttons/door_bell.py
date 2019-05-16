from buttons.base.base_button import BaseButton

class DoorBellButton(BaseButton):    
    def __init__(self):
        super(DoorBellButton, self).__init__()
        self.name = "door_bell"
    
    def action(self, event):
        self.play("doorbell.mp3")

t = DoorBellButton()
t.start()