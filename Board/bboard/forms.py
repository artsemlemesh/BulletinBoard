from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=10)
    class Meta:
        model = Post
        fields = ['author', 'title', 'text']