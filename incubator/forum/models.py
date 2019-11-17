from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse_lazy

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null = False)


    def get_absolute_url(self):
        return reverse_lazy('detail', kwargs={'pk':self.id})

class Comment(models.Model):
    path = ArrayField(models.IntegerField())
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null = False)

    def __str__(self):
        return self.content[0:200]
 
 
 # The shift and the number of columns will organize a tree display of comments on the page,
 #  but the shift is not more than 6 columns, 
 # because at the moment the grid is divided into 12 columns.
    def get_offset(self):
        level = len(self.path) - 1
        if level > 5:
            level = 5
        return level
 
    def get_col(self):
        level = len(self.path) - 1
        if level > 5:
            level = 5
        return 12 - level
