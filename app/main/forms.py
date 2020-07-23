from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms import ValidationError
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.')
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):

    blog_heading = StringField('Travel Blog Title', validators=[Required()])
    blog_content = TextAreaField('Blog contents', validators=[Required()])
    blog_author = StringField('Blog Author', validators=[Required()])
    submit = SubmitField('Submit')

