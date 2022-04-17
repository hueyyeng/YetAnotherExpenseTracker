from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import redirect, render
from django.views import View


class LoginView(View):
    def get(self, request):
        user = request.user
        if not isinstance(user, AnonymousUser):
            return redirect("dashboard")

        form = AuthenticationForm()
        context = {
            "user": user,
            "login_form": form,
        }
        return render(
            request,
            "login.html",
            context=context,
        )

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        context = {
            "user": user,
        }
        if not user:
            context.update(
                {
                    "error": "Invalid username or password",
                }
            )
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
        return redirect("login")


def home_page(request):
    print(f"{request.user=}")
    user = request.user
    if isinstance(user, AnonymousUser):
        return redirect("login")

    return redirect("dashboard")
