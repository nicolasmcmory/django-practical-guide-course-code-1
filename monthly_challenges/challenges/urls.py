from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>", views.challenges_by_month_int),
    path("<str:month>", views.challenges_by_month_str, name="challenges_by_month"),
]
