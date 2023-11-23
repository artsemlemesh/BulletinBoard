from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import PostForm

class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    #paginate_by = 4

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'



class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_update.html'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'
    #permission_required = check later

