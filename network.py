from flask_script import Server, Manager, prompt, prompt_bool
from flask_migrate import Migrate, MigrateCommand
# from app import app, app_db
from network_app import manager as app_manager
from network_app import app
from utils.networking import Networking
import configparser
import subprocess
import sys
import os
import io

manager = Manager(app)
ip = Networking.get_ip_address()
manager.add_command("start", Server(host=ip,use_debugger=True, port=6000))

if __name__ == "__main__":
    try:
        manager.run()
    except:
        app_manager.stop()