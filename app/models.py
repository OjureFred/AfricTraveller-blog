from . import db
from . import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
class Blog(db.Model):
    '''
    Blog class to define blog objects
    '''
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    heading = db.Column(db.String(40))
    content = db.Column(db.String(3000))
    date = db.Column(db.String(10))
    author = db.Column(db.String(40))
    picture = db.Column(db.String(150))

    def __repr__(self):
        return f'Blog {self.heading}'
    
    
class Comment(db.Model):
    '''
    Comment class to define comment objects
    '''
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer)
    details = db.Column(db.String(500))
    date = db.Column(db.String(20))

    def __repr__(self):
        return f'Comment {self.details}'
    
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref = 'role', lazy = "dynamic")

    def __repr__(self):
        return f'Role {self.name}'



