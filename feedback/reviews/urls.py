# Reviews_App:urls.py
from django.urls import path
from . import views

urlpatterns = [path("", views.review, name="reviews")]
