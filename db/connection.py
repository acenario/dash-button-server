import configparser
from sqlalchemy.schema import CreateSchema
from sqlalchemy_utils import database_exists, create_database

def init_db(db_type):
    config = configparser.ConfigParser()
    config.read('config.ini')
    url = ""
    initial = False
    init = ""

    try:
        url = config.get('database', 'database_url')
    except:
        if db_type == "postgres":
            url = "postgresql://localhost/ai_ira_helper"
            if not database_exists(url):
                init = CreateSchema('ai_ira_helper')
                create_database(url)
                initial = True
        else:
            url = "sqlite:////tmp/test.db"
    
    db_init = {"url": url, "initial": initial,"init": init}
    
    return db_init