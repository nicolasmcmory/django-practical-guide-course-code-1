from django.urls import path
from . import views

urlpatterns = [
    path("reviews", views.ReviewsView.as_view(), name="reviews"),
    path("", views.home, name=""),
    path("review", views.ReviewView.as_view(), name="review"),
    path("thank-you", views.ThankYouView.as_view(), name="thanks"),
    path("reviews/<int:review_id>", views.ReviewDetail.as_view(), name="review-detail"),
]
