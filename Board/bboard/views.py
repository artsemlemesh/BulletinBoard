from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from .models import DisposableCode
from django.core.mail import send_mail
import random
# from .signals import send_confirmation_email
import secrets
from django.contrib.auth import authenticate, login
from django.dispatch import receiver

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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print('register FUNCTION')
        if form.is_valid():
            user = form.save()
            disposable_code = DisposableCode.objects.create(user=user, code = generate_unique_code())
            send_confirmation_email(user, disposable_code.code)
            print('send_confirmation_email')
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def generate_unique_code():
    while True:
        code = secrets.token_urlsafe(10)
        print('generate_unique_code FUNCTION')
        if not DisposableCode.objects.filter(code=code).exists():
            break
    return code

def send_confirmation_email(user, confirmation_code):
    subject = 'Account confirmation email'
    message = f'Hello {user.username}, \n\nPlease confirm your registration by clicking the following link:\n\nhttp://127.0.0.1:8000/bboard/confirm/{confirmation_code}'
    send_mail(subject, message, ['Artsemlemesh@yandex.by'], ['bublikteam1@gmail.com'])
    print('send_confirmation_email function')







def confirmation(request, confirmation_code):
    # try:
    disposable_code = DisposableCode.objects.get(code=confirmation_code)
    print('CONFIRMATION')
    disposable_code.user.is_active = True
    disposable_code.user.save()
    disposable_code.delete()
    return render(request, 'registration/confirmation_success.html')
    # except DisposableCode.DoesNotExist:
    #     return render(request, 'registration/confirmation_error.html')











