from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="book-outlet-landing"),
    path("<slug:slug>", views.book_detail, name="book-detail"),
]
