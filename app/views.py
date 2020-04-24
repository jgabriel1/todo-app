from flask import render_template, redirect
from datetime import datetime
from . import app
from .forms import TaskForm, TaskCompleteForm
from .models import db, Task


@app.route('/', methods=['GET', 'POST'])
def index():
    tasks_list = Task.query.all()

    for task in tasks_list:
        task.complete_form = TaskCompleteForm(
            default=task.completed  # View FlaskForm docs;
        )

        if task.complete_form.validate_on_submit():
            task_model_instance = Task.query.filter_by(
                description=task.description
            ).first()
            task_model_instance.completed = not task_model_instance.completed
            db.session.commit()

    form = TaskForm()

    if form.validate_on_submit():
        new_task = Task(
            description=form.description.data,
            completed=False,
            created_at=datetime.utcnow(),
            finished_at=None
        )

        db.session.add(new_task)
        db.session.commit()

        return redirect('/')

    return render_template('index.html', form=form, tasks_list=tasks_list)
