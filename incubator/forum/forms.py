from django import forms
from .models import Post
from django.forms import ModelForm


class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
