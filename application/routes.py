from application import app, db
from application.forms import TaskForm
from application.models import Tasks
from flask import render_template, request, redirect, url_for

@app.route('/')
def index():
    all_tasks = Tasks.query.all()
    return render_template('index.html', all_tasks=all_tasks)

@app.route('/new_task', methods=['GET', 'POST'])
def new_task():
    form = TaskForm()

    if request.method == "POST":
        task = Tasks(description=form.description.data)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('new_task.html', form=form)


