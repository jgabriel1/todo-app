from flask import render_template
from datetime import datetime
from app import app
from app.forms import TaskForm
from app.models import db, Task


@app.route('/', methods=['GET', 'POST'])
def index():
    tasks_list = Task.query.all()

    form = TaskForm()

    if form.validate_on_submit():
        new_task = Task(
            description=form.description.data,
            completed=True,
            created_at=datetime.utcnow(),
            finished_at=None
        )

        db.session.add(new_task)
        db.session.commit()

    return render_template('index.html', form=form, tasks_list=tasks_list)
