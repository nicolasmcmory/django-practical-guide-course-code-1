from django.test import TestCase
from .forms import ReviewForm


# Create your tests here.
class ReviewFormTest(TestCase):
    def test_review_form_valid(self):
        form_data = {
            "user_name": "John Doe",
            "review_text": "Great product!",
            "rating": "5",
        }
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_review_form_invalid(self):
        form_data = {
            "user_name": "",
            "review_text": "",
            "rating": "",
        }
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())
