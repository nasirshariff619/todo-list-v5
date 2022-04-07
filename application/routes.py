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

@app.route('/complete/<completed>/<int:id>')
def complete_task(completed, id):
    task = Tasks.query.get(id)
    if completed == 'True':
        task.completed = True
        db.session.commit()
    elif completed == 'False':
        task.completed = False
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_task(id):
    task = Tasks.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))


