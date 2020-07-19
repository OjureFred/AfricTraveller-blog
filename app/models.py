class Blog:
    '''
    Blog class to define blog objects
    '''
    all_blogs = []

    def __init__(self, id, heading, content, date, author, picture):
        self.id = id
        self.heading = heading
        self.content = content
        self.date = date
        self.author = author
        self.picture = picture
    
    def save_blog(self):
        Blog.all_blogs.append(self)
    
    @classmethod
    def clear_blogs(cls):
        Blog.all_blogs.clear()
    
   
class Comment:
    '''
    Comment class to define comment objects
    '''
    all_comments = []

    def __init__(self, id, blog_id, details, date):
        self.id = id
        self.blog_id = blog_id
        self.details = details
        self.date = date
    
    def save_comment(self):
        Comment.all_comments.append(self)

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()
    
    @classmethod
    def get_comments(cls, id):

        response = []

        for comment in cls.all_comments:
            if comment.blog_id == id:
                response.append(comment)
        
        return response


