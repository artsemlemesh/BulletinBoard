from django import forms
from .models import Post, Comment, Author
from django.forms.widgets import FileInput, TextInput, ClearableFileInput
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=10)
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'category']

    widgets = {
        'title': TextInput(attrs={'class': 'form-control'}),
        'text': CKEditorWidget(attrs={'class': 'form-control'}),
    }


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            basic_group = Group.objects.get(name='basic')
            basic_group.user_set.add(user)
        return user


class CommentForm(forms.ModelForm):
    text = forms.CharField(min_length=10)
    class Meta:
        model = Comment
        fields = ['author', 'post', 'text']


# from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
#
#
# class BasicSignupForm(SignupForm):
#     def save(self, request, commit=True):
#         user = super().save(commit=False)
#         user.is_active = False
#         if commit:
#             user.save()
#             author = Author(user=user)
#             author.save()
#             basic_group = Group.objects.get(name='basic')
#             basic_group.user_set.add(user)
#         return user
