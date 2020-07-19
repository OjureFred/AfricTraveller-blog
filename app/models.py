from . import db
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
    
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'



