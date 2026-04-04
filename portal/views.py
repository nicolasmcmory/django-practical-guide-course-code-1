from django.shortcuts import render
from django.views import View
from .services import UserInterface
from . import forms


class UsersView(View):
    def get(self, request):
        users = UserInterface().get_all_users()
        return render(request, "portal/users.html", {"users": users})


class NewUserView(View):

    def post(self, request):
        user_rw = UserInterface()
        form = forms.UserForm(request.POST)

        if form.is_valid():
            user_rw.create_user(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"],
            )
            return render(request, "portal/users.html")
        else:
            return render(request, "portal/new_user_form.html", {"form": form})

    def get(self, request):
        return render(request, "portal/new_user_form.html", {"form": forms.UserForm()})
