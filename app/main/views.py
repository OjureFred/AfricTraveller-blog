from flask import render_template, request, redirect, url_for
from . import main
from flask_login import login_required
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