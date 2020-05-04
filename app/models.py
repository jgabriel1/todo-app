from . import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import post_load
from datetime import datetime

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, nullable=True, default=False)
    created_at = db.Column(db.DateTime, nullable=True)
    finished_at = db.Column(db.DateTime, nullable=True)


class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'description', 'completed')

    @post_load
    def make_task(self, data, **kwargs):
        return Task(**data)


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
