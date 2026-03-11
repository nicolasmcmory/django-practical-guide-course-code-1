from django.urls import path
from .views import CreateProfile, ProfilesHome

urlpatterns = [
    path(
        "",
        ProfilesHome.as_view(),
        name="profiles-home",
    ),
    path(
        "create-profile/",
        CreateProfile.as_view(),
        name="create-profile",
    ),
]
