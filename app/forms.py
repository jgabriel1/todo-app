from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    description = TextField(id='new-task', validators=[DataRequired()])
    submit = SubmitField(id='submit-task', description='Submit')


class TaskCompleteForm(FlaskForm):
    completed = BooleanField(id='task-completed')
    submit = SubmitField(id='submit-completion', label='not_submit')
