from app.models import Comment, User
from app import db

def setUp(self):
    self.user_fred = User(username='Fred', password='majali', email='thefred@ms.com')
    self.new_comment = Comment(blog_id=1234, details='A blog comment', user=self.user_fred)

def tearDown(self):
    Comment.query.delete()
    User.query.delete()

def test_check_instance_variables(self):
    self.assertEquals(self.new_comment.blog_id,1234)
    self.assertEquals(self.new_comment.details,'A blog comment')
    self.assertEquals(self.new_user.user, self.user_fred)

def test_save_comment(self):
    self.new_comment.save_comment()
    self.assertTrue(len(Comment.query.all()) > 0)
        
def test_get_comment_by_id(self):

    self.new_comment.save_review()
    got_comments = Comment.get_comments(1234)
    self.assertTrue(len(got_comments) == 1)
