from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView, FormView
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.urls import reverse_lazy
from django.template.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist


class HomeView(TemplateView):
    template_name = "forum/home.html"


class PostListView(ListView):
    template_name = "forum/forum.html"
    model = Post
    queryset = Post.objects.order_by('-created')
    paginate_by = 10


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


class PostDetailView(DetailView):
    model = Post
    template_name = 'forum/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        context.update(csrf(self.request))
        user = self.request.user
        # Put in the context of all the comments that are relevant to the article 
        # simultaneously sorting them along the way, the auto-increment ID, 
        # so the problems with the hierarchy should not have any comments yet
        context['comments'] = post.comment_set.all().order_by('path')
        context['next'] = post.get_absolute_url()
        # We add form only if the user is authenticated
        if user.is_authenticated:
            context['form'] = CommentForm
        return context


class CreateCommentView(FormView):
    form_class = CommentForm
    template_name = "forum/post_detail.html"

    def get_success_url(self):
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        if post:
            return reverse_lazy('detail',kwargs={'pk':post.id})
        else:
            return reverse_lazy('forum')

    def form_valid(self, form):
        item = Comment()
        item.path = []
        item.author = self.request.user
        item.post = get_object_or_404(Post, id=self.kwargs['pk'])
        item.content = form.cleaned_data['comment_area']
        item.save()
        try:
            item.path.extend(Comment.objects.get(id=form.cleaned_data['parent_comment']).path)
            item.path.append(item.id)
        except ObjectDoesNotExist:
            item.path.append(item.id)
 
        item.save()
        return super().form_valid(form)

