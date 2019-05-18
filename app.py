from flask import Flask, request, json, g, render_template, redirect
from twilio.twiml.voice_response import Gather, VoiceResponse
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
try:
    app.config.from_pyfile('local_config.cfg')
except FileNotFoundError:
    app.config.from_pyfile('sample_config.cfg')
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

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    from_number = request.values.get('Caller')
    # to_number = request.values.get('Called')

    resp = VoiceResponse()

    if from_number == "+19788073607" or from_number == "+16173540817":
        # Read a message aloud to the caller
        resp.play("https://instaud.io/_/3GEH.mp3")
        resp.say("Welcome to Game of Thrones.", voice='man', language="en-GB")
        resp.say("The door will now open. Enjoy the night.", voice='man', language="en-GB")
        resp.play('', digits='ww9')
        resp.say("If you can hear this message, Arjun messed up. Just text him.", voice='man', language="en-GB")

        
        # gather = Gather(action="/door", method="POST")
        # gather.say("Welcome to Game of Thrones night. \n Please enter the code to enter.", voice='man', language="en-GB")

        # resp.append(gather)

        return str(resp)

    return resp

# @app.route("/door", methods=['GET', 'POST'])
# def doorcode():
#     """Respond to incoming phone calls with a brief message."""
#     # Start our TwiML response
#     from_number = request.values.get('Caller')
#     # to_number = request.values.get('Called')

#     resp = VoiceResponse()

#     if from_number == "+19788073607" or from_number == "+16173540817":
#         # Read a message aloud to the caller
#         resp.play("https://instaud.io/_/3GEH.mp3")
#         gather = Gather(action="/door")
#         resp.say("Welcome to Game of Thrones night.", voice='man', language="en-GB")

#         return str(resp)

#     return resp

    

### MAIN
if __name__ == "__main__":
    app.run()