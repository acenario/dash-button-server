import os
import time
import asyncio
import subprocess
from app import manager, app
from buttons.base.base_apple_tv_button import AppleTVButton

class LatestViceButton(AppleTVButton):    
    def __init__(self):
        super(LatestViceButton, self).__init__()
        self.name = "play_vice"

    def play_vice(self):
        commands = [
            [
                ("menu", 1) #GO TO HOME
            ],
            [
                ("left", 7),
                ("up", 8),
                ("down", 1),
                ("right", 2),
                ("select", 1) #OPEN HBO
            ],
            [
                ("up", 10),
                ("right", 4),
                ("left", 1),
                ("select", 1) #OPEN SEARCH
            ],
            [
                ("left", 30),
                ("right", 23),
                ("select", 1) #SELECT "V"
            ],
            [
                ("left", 13),
                ("select", 1) #SELECT "I" AFTER "V"
            ],
            [
                ("down", 2),
                ("select", 1) #SELECT VICE
            ],
            [
                ("down", 1),
                ("select", 1) #SELECT LATEST EPISODE
            ],
            [
                ("select", 1) #PLAY LATEST EPISODE
            ]
        ]

        print("here?")
        self.send_appletv_commands(commands)


    def action(self, event):
        # self.say("Alexa tell Living Room Playing Latest Episode of Vice")
        self.say("hello")
        self.play_vice()

t = LatestViceButton()
t.start()