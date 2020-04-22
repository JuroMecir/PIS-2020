
import json
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_login import LoginManager, login_user, current_user
from controllers.forms import LoginForm
from controllers.students import Student
from controllers.web_services import Web_service



app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    ws = Web_service()
    temp = ws.students.service.getAll()
    for student in temp:
        if student.id == user_id:
            return student
    return None

@app.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        ws = Web_service()
        for student in ws.students.service.getAll():
            if form.email.data == student.email and form.password.data == student.password:
                flash('You have been logged in!', 'success')
                test = Student(student.id, student.name, student.surname, student.email, student.password, student.date_of_birth, student.address, student.points, student.room_id)
                login_user(test, force=True)
                return redirect(url_for('dashboard'))
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    ws = Web_service()
    number = 0
    if ws.applications.service.getAll():
        for application in ws.applications.service.getAll():
            if application.student_id == current_user.id:
                number += 1
    return render_template('index.html', number = number)

@app.route("/application",methods=['GET','POST'])
def application():
    ws = Web_service()
    rooms = []
    your_app = []
    if ws.applications.service.getAll():
        for application in ws.applications.service.getAll():
            if application.student_id==current_user.id:
                your_app.append(application)


    if ws.rooms.service.getAll():
        for room in ws.rooms.service.getAll():
            if room.type == current_user.sex:
                if len(your_app) == 0:
                    rooms.append(room)
                else:
                    temp = 0
                    for application in your_app:
                        if application.room_id == room.id:
                            temp+=1
                    if temp == 0 :
                        rooms.append(room)

    return render_template('application.html', rooms=rooms)

@app.route("/addApplication",methods=['GET','POST'])
def addApplication():
    ws = Web_service()
    if request.method == 'POST':
        room_id = request.form['room_id']
        ws.applications.service.insert(team_id='093', team_password='FV45AJ', Application={
            'id': 1,
            'name': 'application',
            'student_id': current_user.id,
            'room_id': room_id
        })
    return redirect("/dashboard")



if __name__ == '__main__':
    app.run()
