from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from ..models import Comment, User, Blog
from . import main
from .forms import UpdateProfile, BlogForm, CommentForm
from .. import db, photos
import markdown2

#Views
@main.route('/')
def index():
    '''
    Function to load the index page
    '''
    blog_list = Blog.query.all()

       
    return render_template('index.html', blog_list=blog_list)


@main.route('/blog/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    if form.validate_on_submit():
       #Updated comment instance
       new_comment = Comment(blog_id=id, details=form.blog_details.data, user_id = current_user.id)
       #save comment method
       db.session.add(new_comment)
       db.session.commit()
       return redirect(url_for('main.index'))
        
    title = 'New Comment'
    return render_template('new_comment.html', title= title, comment_form = form)
        

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
    
    return render_template('profile/update.html', form=form)

@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname = uname))

@main.route('/comment/<int:id>')
def single_comment(id):
    comment = Comment.query.get(id)
    if comment is None:
        abort(404)
    
    format_comment = markdown2.markdown(comment.details, extras=['code-friendly', 'fenced-code-blocks'])
    return render_template('comment.html', comment=comment, format_comment=format_comment)

@main.route('/blog/new/', methods=['GET', 'POST'])
def new_blog():
    '''
    Function to allow a user add a new blog post
    '''
    form = BlogForm()
    if form.validate_on_submit():
        new_blog = Blog(heading=form.blog_heading.data, content=form.blog_content.data, author=form.blog_author.data)
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('main.index'))

    title = 'New Blog'
    return render_template('new_blog.html', title = title, blog_form = form)

@main.route('/blog/<int:id>')
def single_blog(id):
    blog = Blog.query.get(id)
    comments = Comment.query.filter_by(blog_id = id).all()
    if blog is None:
        abort(404)

    format_blog = markdown2.markdown(blog.content, extras=["code-friendly", "fenced-code-blocks"])
    return render_template('blog_r.html', blog = blog, comments = comments, format_blog = format_blog)
    
