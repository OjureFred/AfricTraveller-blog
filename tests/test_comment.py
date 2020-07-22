from app.models import Comment, User
from app import db

def setUp(self):
    self.user_fred = User(username='Fred', password='majali', email='thefred@ms.com')
    self.new_comment = Comment(blog_id=1234, details='A blog comment', user=self.user_fred)

def tearDown(self):
    Comment.query.delete()
    User.query.delete()