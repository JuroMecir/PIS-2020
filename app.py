from flask import Flask, render_template, flash
from flask_login import LoginManager, login_user
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
        temp = ws.students.service.getAll()
        for student in temp:
            if form.email.data == student.email and form.password.data == student.password:
                flash('You have been logged in!', 'success')
                test = Student(student.id, student.name, student.surname, student.email, student.password, student.date_of_birth, student.address, student.points, student.room_id)
                login_user(test, force=True)
                return render_template('index.html')
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)










if __name__ == '__main__':
    app.run()
