import configparser
from sqlalchemy.schema import CreateSchema
from sqlalchemy_utils import database_exists

def load_db_url(db_type):
    config = configparser.ConfigParser()
    config.read('config.ini')
    url = ""

    try:
        url = config.get('database', 'database_url')
    except:
        if db_type == "postgres":
            url = "postgresql://localhost/ai_ira_helper"
            if not database_exists(url):
                CreateSchema('ai_ira_helper')
        else:
            url = "sqlite:////tmp/test.db"

    return url