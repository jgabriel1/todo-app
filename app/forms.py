from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, TextField, FieldList, FormField
from wtforms.validators import DataRequired
from collections import OrderedDict


class TaskForm(FlaskForm):
    description = TextField(id='new-task', validators=[DataRequired()])
    submit = SubmitField(id='submit-task', description='Submit')


class SingleTask(FlaskForm):
    completed = BooleanField(id='task-completed')


class TaskCompleteForm(FlaskForm):

    @classmethod
    def from_task_list(cls, task_list: list):
        completed = OrderedDict()
        for i, task in enumerate(task_list):
            setattr(
                cls,
                f'task{i}',
                BooleanField(id=f'task-completed-{i}')
            )
            completed.update({f'task{i}': task.completed})

        setattr(
            cls,
            'submit',
            SubmitField(id='submit-completion', label='Submit Changes')
        )

        return cls(**completed)

    # https://wtforms.readthedocs.io/en/latest/fields/#wtforms.fields.FieldList
