from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your name", max_length=100)
    address = forms.CharField(label="Your address", max_length=100)
