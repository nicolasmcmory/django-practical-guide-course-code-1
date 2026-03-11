import os

from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile


# Create your views here.
class CreateProfile(View):
    # Class-based view to handle profile creation and profile picture upload
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {"form": form})

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            submitted_form.save()
            return HttpResponseRedirect("/profiles/create-profile/")
        else:
            return render(
                request, "profiles/create_profile.html", {"form": submitted_form}
            )


class ProfilesHome(View):
    # Class-based view to render the profiles home page
    def get(self, request):
        # Fetch all user profiles from the database and render them in the template
        profiles = UserProfile.objects.all()
        return render(request, "profiles/profiles_home.html", {"profiles": profiles})
