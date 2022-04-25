from __future__ import annotations

import calendar
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.db.models import QuerySet
    from django.http import HttpRequest
    from django.contrib.admin import ModelAdmin

from datetime import datetime

from django.contrib import admin
from django.contrib.admin import DateFieldListFilter, SimpleListFilter
from django.utils.translation import gettext_lazy as _

from tracker.models import Expense, ExpenseType, ExpenseConfig


class TransactionYearFilter(SimpleListFilter):
    # Repurpose from https://stackoverflow.com/a/62767071/8337847
    title = str(_("Year"))
    parameter_name = str(_("year"))

    def lookups(self, request: HttpRequest, model_admin: ModelAdmin) -> list:
        qs = model_admin.model.objects.exclude(
            transaction_dt=None,
        ).order_by(
            "transaction_dt"
        )
        first_year = qs[0].transaction_dt.year
        current_year = datetime.now().year
        return [(y, y) for y in range(first_year, current_year + 1)]

    def queryset(self, request: HttpRequest, queryset: QuerySet) -> QuerySet:
        if self.value():
            return queryset.filter(transaction_dt__year=int(self.value()))

        return queryset


class TransactionMonthFilter(SimpleListFilter):
    # Repurpose from https://stackoverflow.com/a/62767071/8337847
    title = str(_("Month"))
    parameter_name = str(_("month"))

    def lookups(self, request: HttpRequest, model_admin: ModelAdmin) -> list:
        months = [
            (m, calendar.month_name[m]) for m in range(1, 13)
        ]
        return months

    def queryset(self, request: HttpRequest, queryset: QuerySet) -> QuerySet:
        if self.value():
            return queryset.filter(transaction_dt__month=int(self.value()))

        return queryset


@admin.register(ExpenseType)
class ExpenseTypeAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "description",
    )

    readonly_fields = (
        "created_dt",
        "modified_dt",
    )

    list_display = (
        "id",
        "name",
        "description",
    )

    search_fields = (
        "name",
        "description",
    )


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "description",
        "amount",
        "type",
        "transaction_dt",
    )

    readonly_fields = (
        "created_dt",
        "modified_dt",
    )

    list_display = (
        "id",
        "name",
        "amount",
        "transaction_dt",
    )

    list_filter = (
        ("transaction_dt", DateFieldListFilter),
        TransactionYearFilter,
        TransactionMonthFilter,
    )

    search_fields = (
        "name",
        "description",
        "amount",
    )

    date_hierarchy = "transaction_dt"


@admin.register(ExpenseConfig)
class ExpenseConfigAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "description",
        "config",
    )

    readonly_fields = (
        "created_dt",
        "modified_dt",
    )

    list_display = (
        "id",
        "name",
        "description",
        "config",
    )

    search_fields = (
        "name",
        "description",
        "config",
    )
