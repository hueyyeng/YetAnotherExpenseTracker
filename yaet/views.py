from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View


class LoginView(View):
    def get(self, request):
        user = request.user
        if not isinstance(user, AnonymousUser):
            return redirect("dashboard")

        form = AuthenticationForm()
        context = {
            "login_form": form,
        }
        return render(
            request,
            "login.html",
            context=context,
        )

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        context = {
            "login_form": form,
        }
        if not form.is_valid():
            return render(
                request,
                "login.html",
                context=context,
            )

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            return render(
                request,
                "login.html",
                context=context,
            )

        login(request, user)
        messages.info(request, f"You are now logged in as {username}.")
        return redirect("dashboard")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponse("You Are Already Logout Desu!")


def home_page(request):
    print(f"{request.user=}")
    user = request.user
    if isinstance(user, AnonymousUser):
        return redirect("login")

    return redirect("dashboard")
