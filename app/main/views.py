from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required
from ..models import Comment, User, Blog
from . import main
from .forms import UpdateProfile
from .. import db, photos
from ..models import Comment
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
    '''
    Function to get a new comment
    '''
    form = CommentForm()
    blog = get_blog(id)
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data

        #Updated comment instane
        new_comment = Comment(blog_id=blog.id, blog_title=title, blog_comment=comment, user=current_user)
        
        #save blog method
        new_blog.save_blog()
        return redirect(url_for('.blog', id=blog.id))
        
    title = f'{blog.title} coment'
    return render_template('new_blog.html', title = title, review_form = form, blog = blog)
        

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

@main.route('/blog/<int:id>')
def single_blog(id):
    blog = Blog.query.get(id)
    if comment is None:
        abort(404)

    format_blog = markdown2.markdown(blog.content, extras=["code-friendly", "fenced-code-blocks"])
    return render_template('blog_r.html', blog = blog, format_blog = format_blog)
    
