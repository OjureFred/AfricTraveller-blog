from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required
from ..models import Comment, User
from . import main
#from .forms import CommentForm
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

    return render_template("profile/profile.html", user = user)
