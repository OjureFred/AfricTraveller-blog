from flask import render_template
from ..models import User
from .forms import RegistrationForm
from .. import db
from . import auth

@auth.route('/login')
def login():
    return render_template('auth/login.html')
    pass

@auth.route('/register', methods=["GET", "post"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        title = "New Account"
    return render_template('/auth/register.html', registration_form = form)