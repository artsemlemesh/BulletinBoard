from datetime import timedelta
from django.utils import timezone


from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = RichTextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('bboard:post_detail', args=[str(self.id)])

class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'Reaction on {self.author}\'s {self.post}'

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DisposableCode(models.Model):
    code = models.CharField(max_length=255, unique=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=timezone.localtime(timezone.now()) + timedelta(minutes=1))

    def __str__(self):
        return f'Disposable code: {self.code}'





