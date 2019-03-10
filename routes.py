from flask import Flask, render_template, request

app = Flask(__name__)

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