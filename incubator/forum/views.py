from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView, FormView
from .models import Post
from .forms import CommentForm, PostForm
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = "forum/home.html"

class PostListView(ListView):
    template_name = "forum/forum.html"
    model = Post
    queryset = Post.objects.order_by('-created')
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = 'forum/post_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_comment'] = CommentForm()
        return context

class CreatePostView(FormView):
    template_name = "forum/create_post.html"
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('forum')

    def form_valid(self, form):
        item = form.save(commit=False)
        item.author = self.request.user
        item.save()
        return super().form_valid(form)