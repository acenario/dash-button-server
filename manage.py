from flask_script import Server, Manager, prompt, prompt_bool
from flask_migrate import Migrate, MigrateCommand
from app import app, db
from app import manager as app_manager
from utils.networking import Networking
import configparser
import subprocess
import sys
import os
import io

manager = Manager(app)
migrate = Migrate(app, db)
ip = Networking.get_ip_address()
manager.add_command("runserver", Server(host=ip))
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    try:
        manager.run()
    except:
        app_manager.stop()