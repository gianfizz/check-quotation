from rest_framework import serializers

from app.models.expenses_model import ExpensesModel


class ExpensesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpensesModel
        fields = [
            "uuid", "discount_rate", "payment_date_discount"
            ]
