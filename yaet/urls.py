from django.contrib import admin
from django.urls import path, include

from yaet.views import LoginView, LogoutView, home_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tracker/", include("tracker.urls")),
    path(
        "login/",
        LoginView.as_view(),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
    path(
        "",
        home_page,
        name="home",
    ),
]
