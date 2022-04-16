from django.urls import path

from tracker.api import ExpenseAPI
from tracker.views import DashboardView

urlpatterns = [
    path(
        "api/expense/",
        ExpenseAPI.as_view(),
        name="expense",
    ),
    path(
        "dashboard/",
        DashboardView.as_view(),
        name="dashboard",
    ),
]
