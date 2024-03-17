from django.db import models
from django.utils import timezone
from datetime import timedelta

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete = models.DO_NOTHING,related_name ="posts", default=None)

    def __str__(self):
        return self.title
    
    def published_recently(self):    
        return timezone.now()-timedelta(days=7) < self.published_date
    
class Comment(models.Model):
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete = models.DO_NOTHING, default = None, related_name="comments")
    created_time = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.text