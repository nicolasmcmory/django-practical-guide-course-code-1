from django.urls import path
from . import views

urlpatterns = [
    path("", views.challenges, name="challenges"),
    path("<int:month>", views.challenges_by_month_int),
    path("<str:month>", views.challenges_by_month_str, name="challenges_by_month"),
]
