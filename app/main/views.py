from flask import render_template, request, redirect, url_for
from . import main
from .forms import CommentForm
from ..models import Comment

#Views
@main.route('/')
def index():
    '''
    Function to load the index page
    '''