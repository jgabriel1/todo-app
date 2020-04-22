from . import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy(app)


class Task(db.Model):

    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, nullable=True, default=False)
    create_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    finish_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
