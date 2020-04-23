from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):

    description = TextAreaField(
        label='New Task', id='new-task', validators=[DataRequired()])
    submit = SubmitField(id='submit-task', description='Submit')


class ListTaskForm(FlaskForm):

    completed = 1
