from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "img"]
        widgets = {
            "title": forms.TextInput(),
            "content": forms.Textarea(),
            "img": forms.ClearableFileInput(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["user_name", "user_email", "content"]
        widgets = {
            "user_name": forms.TextInput(),
            "user_email": forms.EmailInput(),
            "content": forms.Textarea(),
        }
