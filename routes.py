from flask import Flask, render_template, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
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
        fields = ('taskname', 'completedate','category')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('kanban.html')

@app.route('/form_update', methods=['GET', 'POST'])
def form_update():

    if request.form['taskcategory'] == "To Do":
        return render_template('kanban.html', update_todo=request.form['taskname'])
    elif request.form['taskcategory'] == "Doing":
        return render_template('kanban.html', update_doing=request.form['taskname'])
    else:
        return render_template('kanban.html', update_done=request.form['taskname'])

if __name__ == "__main__":
    app.run()