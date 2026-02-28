from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your name", max_length=100)
