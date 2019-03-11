from app import app_db, manager
from sqlalchemy.dialects.postgresql import JSON, DATE
import time
from sqlalchemy.sql import func

class Button(app_db.Model):
    __tablename__ = 'Button'

    id = app_db.Column(app_db.Integer, primary_key=True)
    name = app_db.Column(app_db.String(255))
    mac = app_db.Column(app_db.String(255), unique=True)
    style = app_db.Column(app_db.String(255))
    last_pushed = app_db.Column(app_db.Float)
    created_at = app_db.Column(app_db.DateTime, default=func.now())
    updated_at = app_db.Column(app_db.DateTime, onupdate=func.now())

    def __init__(self, name, mac, style):
        self.name = name
        self.mac = mac
        self.style = style
        self.last_pushed = time.time()

    def __repr__(self):
        return '<name: {}, mac: {}, style: {}>'.format(self.name, self.mac, self.style)

    @classmethod
    def get_button_cache(self):
        buttons = self.query.all()
        cache = {}
        for btn in buttons:
            k = btn.mac
            cache[k] = {"name": btn.name,
                        "style": btn.style,
                        "btn_id": btn.id,
                        "last_pushed": btn.last_pushed}

        return cache

    @classmethod
    def should_register_push(self, btn_id, cooldown):
        btn = self.query.get(btn_id)
        lt = btn.last_pushed
        ct = time.time()
        diff = ct - lt
        if (diff > 5):
            btn.last_pushed = ct
            app_db.session.commit()
            manager.cache["buttons"] = Button.get_button_cache()
            return True
            
        return False