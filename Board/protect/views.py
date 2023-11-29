from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters import FilterSet

from bboard.models import Post, Comment
from django.contrib.auth.models import Group

class PostFilter(FilterSet):
    class Meta:
        model = Comment
        fields = ['post']

    def __init__(self, *args, **kwargs):
        super(PostFilter, self).__init__(*args, **kwargs)
        self.filters['post'].queryset = Post.objects.filter(author__user_id=kwargs['request'])

class IndexView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'protect/index.html'
    context_object_name = 'comments'

    def get_queryset(self):
        queryset = Comment.objects.filter(post__author__user_id=self.request.user.id).order_by('-date')
        self.filterset = PostFilter(self.request.GET, queryset, request=self.request.user.id)
        if self.request.GET:
            return self.filterset.qs
        return Comment.objects.none()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    def delete_comment(request, comment_id):
        comment = Comment.objects.get(pk=comment_id)
        comment.delete()
        return HttpResponseRedirect('/')

    # class PostDelete(DeleteView):
    #     model = Post
    #     template_name = 'post_delete.html'
    #     success_url = reverse_lazy('post_list')

    def accept_comment(request, comment_id):
        comment = Comment.objects.get(pk=comment_id)
        comment.status = True
        comment.save()
        return HttpResponseRedirect('/')


