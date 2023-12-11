from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User             ## auth is the app, user is the class

# Create your models here.

### blog_post           the name of the table must be the name of the app underscore name of the class
class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title