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

        current_month = datetime.datetime.now().month
        expenses = []
        _expenses = Expense.objects.filter(
            transaction_dt__month=current_month,
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
