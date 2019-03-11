from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taskname = db.Column(db.String(80), unique=True)
    completedate = db.Column(db.DateTime())
    category = db.Column(db.String(20))

    def __init__(self, taskname, completedate, category):
        self.taskname = taskname
        self.completedate = completedate
        self.category = category

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id','taskname', 'completedate','category')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


@app.route('/', methods=['GET', 'POST'])
def form():
    all_tasks = Task.query.all()
    result = tasks_schema.dump(all_tasks).data

    to_do = []
    doing = []
    done = []
    
    for i in result:
        if datetime.strptime(i['completedate'][:10], '%Y-%m-%d') > datetime.today():
            i['overdue'] = False
        else:
            i['overdue'] = True
        if i['category'] == 'To Do':
            to_do.append(i)
        elif i['category'] == 'Doing':
            doing.append(i)
        else:
            done.append(i)

    to_do.sort(key=lambda r: r['completedate'])
    doing.sort(key=lambda r: r['completedate'])
    done.sort(key=lambda r: r['completedate'])

    return render_template('kanban.html', update_todo=to_do, update_doing=doing, update_done=done)

@app.route('/form_update', methods=['GET', 'POST'])
def form_update():
    taskname = request.form['taskname']
    completedate = datetime.strptime(request.form['completedate'], '%Y-%m-%d')
    taskcategory = request.form['taskcategory']

    new_task = Task(taskname, completedate, taskcategory)

    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for('form'))

@app.route('/move_task/<task_id>/<category>', methods=['GET'])
def move_task(task_id, category):
    task = Task.query.get(task_id)
    if category == 'todo':
        task.category = 'To Do'
    else:
        task.category = category

    db.session.commit()
    return redirect(url_for('form'))

@app.route('/delete_task/<task_id>', methods=['GET'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for('form'))

if __name__ == "__main__":
    app.run()