from flask import render_template, redirect, url_for, request
from datetime import datetime
from . import app
from .forms import TaskForm, TaskCompleteForm
from .models import db, Task


@app.route('/', methods=['GET', 'POST'])
def index():
    tasks_list = sorted(Task.query.all(), key=lambda task: task.id)
    tasks_form = TaskCompleteForm.from_task_list(tasks_list)

    if tasks_form.validate_on_submit():
        results = [
            field.data for field in tasks_form
            if field.name != 'submit'
            if field.name != 'csrf_token'
        ]

        for task, result in zip(tasks_list, results):
            if result != task.completed:
                model_instance = Task.query.filter_by(
                    description=task.description
                ).first()

                if not task.completed:
                    model_instance.finished_at = datetime.utcnow()
                else:
                    model_instance.finished_at = None

                model_instance.completed = not model_instance.completed
                db.session.commit()

    form = TaskForm()

    return render_template(
        'index.html',
        form=form,
        tasks_list=tasks_list,
        tasks_form=tasks_form
    )


@app.route('/new_task', methods=['POST'])
def new_task():
    data = request.form.get('description')

    new_task = Task(
        description=data,
        completed=False,
        created_at=datetime.utcnow(),
        finished_at=None
    )

    db.session.add(new_task)
    db.session.commit()

    return redirect('/')


@app.route('/delete_task/<id>', methods=['POST'])
def delete_task(id):
    """
    This should just do stuff without really returning anything.
    
    """
    return f"<h2>Delete task {id}!</h2>"
