from application import app
from application.forms import TaskForm
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_task', methods=['GET', 'POST'])
def new_task():
    form = TaskForm()
    return render_template('new_task.html', form=form)


