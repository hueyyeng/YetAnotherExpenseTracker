import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect
from django.views import View

from tracker.models import Expense


class DashboardView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request):
        user = request.user
        if isinstance(user, AnonymousUser):
            return redirect("dashboard")

        year = request.GET.get("year"):
        if not year:
            year = datetime.datetime.now().year

        month = request.GET.get("month"):
        if not month:
            month = datetime.datetime.now().month

        expenses = []
        # TODO: Add the F expression to filter both month and year
        _expenses = Expense.objects.filter(
            transaction_dt__month=month,
        )
        for expense in _expenses:
            expense: Expense
            expenses.append(f"{expense.name} - {expense.amount}")

        context = {
            "expenses": expenses,
        }
        return render(
            request,
            "tracker/dashboard.html",
            context=context,
        )
