from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    rating = forms.ChoiceField(
        label="Your Rating",
        choices=RATING_CHOICES,
        widget=forms.RadioSelect,
    )

    class Meta:

        model = Review
        fields = "__all__"
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Review",
        }
