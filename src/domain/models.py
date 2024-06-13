from src.infra.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))


class Alarm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    asset = db.Column(db.String(255))
    target_price = db.Column(db.Float)

    user = db.relationship("User", backref=db.backref("alarms", lazy=True))
