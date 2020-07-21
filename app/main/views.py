from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required
from ..models import Comment, User
from . import main
from .forms import UpdateProfile
from .. import db
from ..models import Comment

#Views
@main.route('/')
def index():
    '''
    Function to load the index page
    '''
    pass

@main.route('/blog/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    '''
    Function to get a new comment
    '''

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)

@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))
    
    return render_template('profile/update.html', form = form)
