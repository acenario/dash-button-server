from flask import Flask, request, json, g, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from manager.manager import AppManager
from utils.networking import Networking
from db import connection
import requests

app = Flask(__name__) 
manager = AppManager()

### MANAGER
manager.load_button_listener()
ip = Networking.get_ip_address()

def fetch_buttons():
    addr = "http://{}:{}/buttons".format(ip,"5000")
    r = requests.get(addr)
    buttons_dict = r.json()
    return buttons_dict

### CACHE
manager.cache["buttons"] = fetch_buttons()


### ROUTES
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['GET'])
def shutdown():
    if request.method == 'GET':
        shutdown_server()
    return 'Server shutting down...'

### MAIN
if __name__ == "__main__":
    app.run()