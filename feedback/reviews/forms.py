from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your name", max_length=50)
    review_text = forms.CharField(
        label="Your feedback", widget=forms.Textarea, max_length=200
    )
    rating = forms.ChoiceField(
        label="Your Rating",
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect,
    )
