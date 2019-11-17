from django import forms
from .models import Post
from django.forms import ModelForm


class CommentForm(forms.Form):
 
    parent_comment = forms.IntegerField(
        widget=forms.HiddenInput,
        required=False
    )
 
    comment_area = forms.CharField(
        label="",
        widget=forms.Textarea
    )


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
