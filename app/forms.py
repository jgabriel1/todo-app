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
        id='submit-task',
        label='Create',
        render_kw={'class_': 'btn btn-primary'}
    )


class TaskCompleteForm(FlaskForm):

    @classmethod
    def from_task_list(cls, task_list: list):
        completed = OrderedDict()
        for i, task in enumerate(task_list):
            setattr(
                cls,
                f'task{i}',
                BooleanField(
                    label=task.description,
                    id=f'task-completed{i}',
                    render_kw={'class_': 'form-check-input'}
                )
            )

            completed.update({f'task{i}': task.completed})

        setattr(
            cls,
            'submit',
            SubmitField(
                id='submit-completion',
                render_kw={
                    'value': 'Submit Changes',
                    'class_': 'btn btn-primary'
                }
            )
        )

        return cls(**completed)

    # https://wtforms.readthedocs.io/en/latest/fields/#wtforms.fields.FieldList
