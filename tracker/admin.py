from django.contrib import admin

from tracker.models import Expense, ExpenseType


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
