from django.shortcuts import render
from django.views.generic import CreateView

from django.views.generic import ListView

from .models import Post

class PostListView(ListView):
    model = Post
    paginate_by = 10

from .models import Comment

class CommentListView(ListView):
    model = Comment
    paginate_by = 10
    
from django.views.generic import DetailView

class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.get_object().id
        context['comment_list'] = Comment.objects.filter(post_id=post_id)
        return context

