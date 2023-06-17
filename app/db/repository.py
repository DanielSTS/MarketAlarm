from app.core.models import User, Alarm
from app.db import db

def create_user(username, password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def create_alarm(user, asset, target_price):
    alarm = Alarm(user=user, asset=asset, target_price=target_price)
    db.session.add(alarm)
    db.session.commit()
    return alarm

def get_alarms_by_user(user):
    return Alarm.query.filter_by(user=user).all()
