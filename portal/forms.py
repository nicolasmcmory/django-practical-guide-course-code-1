from django.forms import ModelForm
from .models import User, Posts


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "image"]

class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ["title", "content", "author"]