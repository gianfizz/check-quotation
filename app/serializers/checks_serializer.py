from rest_framework import serializers

from app.models.checks_model import CheckModel
from app.serializers.expenses_serializer import ExpensesModelSerializer


class CheckModelSerializer(serializers.ModelSerializer):
    expenses = ExpensesModelSerializer(read_only=True)
    class Meta:
        model = CheckModel
        fields = [
            "uuid", "client_check_key", "check_amount", "expiration_date", "quotation_status", "amount_client_recieves", "expenses"
        ]
