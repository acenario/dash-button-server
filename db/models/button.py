from app import app_db
from sqlalchemy.dialects.postgresql import JSON, DATE
from sqlalchemy.sql import func

class Button(app_db.Model):
    __tablename__ = 'Button'

    id = app_db.Column(app_db.Integer, primary_key=True)
    name = app_db.Column(app_db.String(255))
    mac = app_db.Column(app_db.String(255), unique=True)
    style = app_db.Column(app_db.String(255))
    created_at = app_db.Column(app_db.DateTime, default=func.now())
    updated_at = app_db.Column(app_db.DateTime, onupdate=func.now())

    def __init__(self, name, mac, style):
        self.name = name
        self.mac = mac
        self.style = style

    def __repr__(self):
        return '<name: {}, mac: {}, style: {}>'.format(self.name, self.mac, self.style)