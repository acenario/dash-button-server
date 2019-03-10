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
from db.models.button import Button

if (init_db["initial"]):
    app_db.create_all()

### MANAGER
manager = AppManager()
manager.start()

### CACHE
buttons_cache = Button.query.all()

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
                buttons_cache = Button.query.all()
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
        query_arg = request.args.get('v', 'Love you from Ira')
        thread_name = "computer_sleep"
        thread = manager.background_threads[thread_name]
        thread.queue.put(query_arg)
        
        return render_template('index.html', 
                                active1="active", 
                                active11="(current)", 
                                active2="", 
                                active22="",
                                name="",
                                mac="",
                                style="")
    
    return 'Made with love by Arjun & Ira'

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
                buttons_cache = Button.query.all()
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

### MAIN
if __name__ == "__main__":
    app.run()