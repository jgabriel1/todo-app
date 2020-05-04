from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, TextField
from wtforms.validators import DataRequired
from wtforms.widgets import ListWidget
from collections import OrderedDict


class TaskForm(FlaskForm):
    description = TextField(
        id='new-task',
        validators=[DataRequired()],
        render_kw={'placeholder': 'New task...', 'class_': 'form-control'}
    )

    submit = SubmitField(
        label='Create',
        id='submit-task',
        render_kw={'class_': 'btn btn-primary'}
    )
