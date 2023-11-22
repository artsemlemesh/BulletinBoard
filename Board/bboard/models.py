from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = RichTextField()

    def __str__(self):
        return f' post: {self.title}'

    def get_absolute_url(self):
        return reverse('bboard:post_detail', args=[str(self.id)])

class Reaction(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'Reaction on {self.author}\'s {self.post}'