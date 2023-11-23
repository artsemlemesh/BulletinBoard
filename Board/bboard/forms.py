from django import forms
from .models import Post
from django.forms.widgets import FileInput, TextInput, ClearableFileInput
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=10)
    class Meta:
        model = Post
        fields = ['author', 'title', 'text']

    widgets = {
        'title': TextInput(attrs={'class': 'form-control'}),
        'text': CKEditorWidget(attrs={'class': 'form-control'}),
    }
