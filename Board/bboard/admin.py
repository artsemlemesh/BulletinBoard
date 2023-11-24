from django.contrib import admin
from .models import Post, Author, Comment, Category, DisposableCode


admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(DisposableCode)