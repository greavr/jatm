from flask import Flask, render_template, flash, request, redirect
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import googlecloudprofiler

try:
    import googleclouddebugger
    googleclouddebugger.enable()
except ImportError:
    pass


#App config
DEBUG = True
app = Flask(__name__)

taskList = [["Test1","This is a task for fun",0,0],["Test2","This is another task for fun",1,0],["Test3","This is another task for fun",2,0],["Test4","This is another task for fun",3,0],["Test5","This is another task for fun",4,0],["Test6","This is another task for fun",5,0]]

class ReusableForm(Form):
    TaskTitle = TextField('taskTitle:', validators=[validators.required()])
    TaskText = TextField('TaskText:', validators=[validators.required()])

def AddTask(title,body):
    count=len(taskList)
    taskList.append([title,body,count,0])
    return True

def UpdateTask(title,body,complete,id):
    for index, aTask in enumerate(taskList):
        if aTask[2] == id:
            aTask[0] = title
            aTask[1] = body
            aTask[3] = complete
            taskList[index] = aTask
    return True

def GetTasks():
    return taskList

@app.route("/", methods=['GET', 'POST'])
def default():
    form = ReusableForm(request.form)
    allTasks = GetTasks()

    #print(form.errors)
    if request.method == 'POST':
        taskTitle=request.form['TaskTitle']
        TaskText=request.form['TaskText']

        if form.validate():
            flash('Added: {}'.format(taskTitle))
            AddTask(taskTitle,TaskText)
        else:
            flash('Error: All Fields are Required')

    return render_template('index.html', form=form, Tasks=allTasks)

@app.route('/edit/<int:id>', methods=["POST", "GET"])
def task(id):
    form = ReusableForm(request.form)
    allTasks = GetTasks()

    if request.method == 'POST':
        TaskTitle=request.form['TaskTitle']
        TaskText=request.form['TaskText']
        TaskCompleted=request.form.getlist('TaskComplete')
        if not TaskCompleted:
            TaskCompleted = 0
        else:
            TaskCompleted = 1
        TaskID=request.form['TaskID']

        if form.validate():
            UpdateTask(TaskTitle,TaskText,TaskCompleted,TaskID)
            return redirect("/")
        else:
            flash('Error: All Fields are Required')

    for aTask in allTasks:
        if aTask[2] == id:
            editTask = aTask

    return render_template('update.html', form=form, Tasks=allTasks, aTask=editTask)

if __name__ == "__main__":
    # Enable Profiler
    try:
        googlecloudprofiler.start(
            service='hello-profiler',
            service_version='1.0.1',
            verbose=3,
        )
    except (ValueError, NotImplementedError) as exc:
        print(exc)  # Handle errors here

    app.run(host='0.0.0.0', port=8080)