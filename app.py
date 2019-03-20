from flask import Flask, request, json, g, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from manager.manager import AppManager
from db import connection

app = Flask(__name__) 

### DEFAULTS
DB_TYPE = "postgres"

# DATABASE
init_db = connection.init_db(DB_TYPE)
app.config['SQLALCHEMY_DATABASE_URI'] = init_db["url"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app_db = SQLAlchemy(app)
manager = AppManager()
from db.models.button import Button

if (init_db["initial"]):
    app_db.create_all()

### MANAGER
manager.start()

### CACHE
manager.cache["buttons"] = Button.get_button_cache()



### ROUTES
@app.route('/', methods=['POST', 'GET'])
# @requires_ssl
def index():
    """
    This is the index page.
    """     
    if request.method == 'POST':
        form_data = request.form
        name = form_data["buttonName"]
        mac = form_data["macAddress"]
        style = form_data["style"]

        if name and mac:
            btn = Button(name=name, mac=mac, style=style)
            try:
                app_db.session.add(btn)
                app_db.session.commit()
                print("Button stored in DB.")
                manager.cache["buttons"] = Button.get_button_cache()
            except Exception as e:
                print(e)
                error = {}
                error["code"] = 300
                error["error"] = "unable to add item to database: {}".format(btn)
                print(error)

            return render_template('index.html', 
                                    active1="active", 
                                    active11="(current)", 
                                    active2="", 
                                    active22="",
                                    name="",
                                    mac="",
                                    style="")

        return render_template('index.html', 
                                active1="active", 
                                active11="(current)", 
                                active2="", 
                                active22="",
                                name=name,
                                mac=mac,
                                style=style)

    elif request.method == 'GET':
        # query_arg = request.args.get('v', 'Love you from Ira')
        # thread_name = "computer_sleep"
        # thread = manager.background_threads[thread_name]
        # thread.queue.put(query_arg)
        
        return render_template('index.html', 
                                active1="active", 
                                active11="(current)", 
                                active2="", 
                                active22="",
                                name="",
                                mac="",
                                style="")
    
    return 'Made with love by Arjun & Ira'

@app.route('/buttons', methods=['POST', 'GET'])
# @requires_ssl
def get_buttons():
    if request.method == 'POST':
        return json.dumps([{"error": "POST method not allowed" }]), 400
    elif request.method == 'GET':
        manager.cache["buttons"] = Button.get_button_cache()
        return json.dumps(manager.cache["buttons"])
        
    return json.dumps([{"error": "missing application/json content-type or invalid json dict" }]), 400

@app.route('/push', methods=['POST'])
def push_button():
    if request.method == 'POST':
        if request.is_json:
            post_dict = request.get_json()
            if post_dict:
                push_data = post_dict.get("push", None)
                thread_name = push_data["thread_name"]
                cooldown = push_data["cooldown"]
                btn_id = push_data["btn_id"]
                if thread_name in manager.background_threads:
                    if (Button.should_register_push(btn_id, cooldown)):
                        thread = manager.background_threads[thread_name]
                        thread.queue.put(btn_id)
                        return json.dumps([{"success": "registered button push" }]), 200
                    else:                        
                        return json.dumps([{"success": "registered push, but ignored" }]), 200
                return json.dumps([{"error": "missing application/json content-type or invalid json dict" }]), 400
        return json.dumps([{"error": "missing application/json content-type or invalid json dict" }]), 400

@app.route('/editbuttons', methods=['POST', 'GET'])
# @requires_ssl
def edit_buttons():
    """
    This is the index page.
    """     
    buttons = Button.query.all()

    if request.method == 'POST':
        form_data = request.form
        btn_id = form_data["buttonId"]
        name = form_data["buttonName"]
        mac = form_data["macAddress"]
        style = form_data["style"]

        if btn_id and name and mac:
            btn = Button.query.get(btn_id)
            try:
                btn.name = name
                btn.mac = mac
                btn.style = style
                app_db.session.commit()
                print("Button edited in DB.")
                manager.cache["buttons"] = Button.get_button_cache()
            except Exception as e:
                print(e)
                error = {}
                error["code"] = 300
                error["error"] = "unable to edit item in database: {}".format(btn)
                print(error)

        return render_template('edit.html', 
                                active1="", 
                                active11="", 
                                active2="active", 
                                active22="(current)",
                                buttons=buttons)

    elif request.method == 'GET':
        return render_template('edit.html', 
                                active1="", 
                                active11="", 
                                active2="active", 
                                active22="(current)",
                                buttons=buttons)
    
    return 'Made with love by Arjun & Ira'

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