from flask import Flask, render_template, request, redirect, url_for, flash
#from forms import AddTaskForm, CreateUserForm, LoginForm
#from database import Tasks, Users
#from flask_login import LoginManager, login_user, logout_user, login_required, current_user
#from werkzeug.security import generate_password_hash, check_password_hash




app = Flask(__name__)
app.config['SECRET_KEY'] = 'Put Secret String Here!'


@app.route("/", methods=["GET","POST"])
def index():
    return "test"