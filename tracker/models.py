from django.db import models
from django.utils import timezone
from djmoney.models.fields import MoneyField

from utils.mixins import NameDescriptionMixin, CreatedModifiedDtMixin


class ExpenseType(NameDescriptionMixin, CreatedModifiedDtMixin):
    def __str__(self):
        return f"{self.name}"


class Expense(NameDescriptionMixin, CreatedModifiedDtMixin):
    amount = MoneyField(
        max_digits=19,
        decimal_places=4,
        null=True,
        default_currency=None,
    )
    type = models.ForeignKey(
        ExpenseType,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    transaction_dt = models.DateTimeField(
        default=timezone.now,
    )

    def __str__(self):
        transaction_date = self.transaction_dt.strftime("%Y-%m-%d")
        return f"{self.name} - {self.amount} ({transaction_date})"


class ExpenseConfig(NameDescriptionMixin, CreatedModifiedDtMixin):
    config = models.JSONField(
        default=dict,
    )

    def __str__(self):
        return f"{self.name}"

