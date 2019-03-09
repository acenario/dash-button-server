from flask import Flask, request, json, g, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from manager.manager import AppManager
from db import connection

app = Flask(__name__) 

### DEFAULTS
DB_TYPE = "postgres"

# DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = connection.load_db_url(DB_TYPE)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

### MANAGER
manager = AppManager()
manager.start()

### ROUTES
@app.route('/', methods=['POST', 'GET'])
# @requires_ssl
def index():
    """
    This is the index page.
    """     
    if request.method == 'POST':
        post_dict = request.json
        if post_dict:
            data = post_dict.get("v", None)
            if data:
                return json.dumps(data), 200
        return json.dumps([{"error": "missing application/json content-type or invalid json dict" }]), 400

    elif request.method == 'GET':
        query_arg = request.args.get('v', 'Love you from Ira')
        manager.main_queue.put("hello")
        
        return render_template('index.html')
    
    return 'Made with love by Arjun & Ira'

### MAIN
if __name__ == "__main__":
    app.run()