from django.forms import Form, CharField, ModelForm
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "image"]
