import datetime

from django.db.models import F, Func, CharField, Value
from djmoney.money import Money
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tracker.models import Expense, ExpenseType, ExpenseConfig

def get_expenses(current_month: int):
    expenses = Expense.objects.filter(
        transaction_dt__month=current_month,
    ).values(
        "id",
        "name",
        "description",
        "amount",
    ).annotate(
        type=F("type__name"),
        amount_currency=F("amount_currency"),
        transaction_dt=Func(
            Value("%d/%m/%Y"),
            F("transaction_dt"),
            function="strftime",
            output_field=CharField(),
        )
    )

    return expenses


class ExpenseAPI(APIView):
    def get(self, request, format=None):
        current_month = datetime.datetime.now().month
        expenses = get_expenses(current_month)

        expense_types = ExpenseType.objects.values(
            "id",
            "name",
        )

        expense_config = ExpenseConfig.objects.values(
            "config",
        ).first()

        data = {
            "expenses": expenses,
            "expense_types": expense_types,
            "expense_config": expense_config,
        }

        return Response(
            data,
            status=status.HTTP_200_OK,
        )

    def post(self, request, format=None):
        request_data = request.data
        processed_data = []
        for data in request_data:
            transaction_dt = datetime.datetime.strptime(
                data["transaction_dt"],
                "%d/%m/%Y"
            )
            amount = Money(
                data["amount"],
                data["amount_currency"],
            )
            description = data.get("description", "")
            expense = Expense(
                name=data["name"],
                description=description,
                amount=amount,
                type_id=data["type"],
                transaction_dt=transaction_dt,
            )
            processed_data.append(expense)

        Expense.objects.bulk_create(processed_data)

        current_month = datetime.datetime.now().month
        new_expenses = get_expenses(current_month)

        data = {
            "expenses": new_expenses,
        }

        return Response(
            data,
            status=status.HTTP_200_OK,
        )


class ExpenseConfigAPI(APIView):
    def get(self, request, format=None):
        request_data = request.data
        expense_config = ExpenseConfig.objects.get(pk=request_data["id"])

        data = {
            "expense_config": expense_config,
        }

        return Response(
            data,
            status=status.HTTP_200_OK,
        )

    def post(self, request, format=None):
        request_data = request.data
        print(f"{request_data=}")

        data = {}

        return Response(
            data,
            status=status.HTTP_200_OK,
        )
