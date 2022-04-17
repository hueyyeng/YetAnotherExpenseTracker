import datetime

from django.db.models import F
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tracker.models import Expense


class ExpenseAPI(APIView):
    def get(self, request, format=None):
        current_month = datetime.datetime.now().month
        expenses = Expense.objects.filter(
            transaction_dt__month=current_month,
        ).values().annotate(
            type=F("type__name"),
        )

        return Response(
            expenses,
            status=status.HTTP_200_OK,
        )
