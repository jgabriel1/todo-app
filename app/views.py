from flask import render_template, redirect, url_for, request
from datetime import datetime
from . import app
from .forms import TaskForm
from .models import db, Task, tasks_schema


@app.route('/', methods=['get', 'post'])
def index():
    form = TaskForm()
    return render_template('index.html', form=form)


@app.route('/task_list', methods=['get'])
def task_list():
    tasks = sorted(Task.query.all(), key=lambda task: task.id)
    return tasks_schema.dumps(tasks)


@app.route('/complete_tasks', methods=['post'])
def complete_tasks():
    tasks = Task.query.all()
    results = tasks_schema.load(request.get_json())

    # Making sure everything aligns to compare:
    assert len(tasks) == len(results)
    tasks.sort(key=lambda task: task.id)
    results.sort(key=lambda task: task.id)

    for task, result in zip(tasks, results):
        if result.completed != task.completed:
            model_instance = Task.query.filter_by(id=task.id).first()

            if not task.completed:
                model_instance.finished_at = datetime.utcnow()
            else:
                model_instance.finished_at = None

            model_instance.completed = not model_instance.completed
            db.session.commit()

    return redirect('/')


@app.route('/new_task', methods=['post'])
def new_task():
    data = request.get_json().get('description')

    new_task = Task(
        description=data,
        completed=False,
        created_at=datetime.utcnow(),
        finished_at=None
    )

    db.session.add(new_task)
    db.session.commit()

    return redirect('/')


@app.route('/delete_task/<id>', methods=['post'])
def delete_task(id):
    to_delete = Task.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect('/')
