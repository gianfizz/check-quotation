import uuid

from django.db import models

from app.models.checks_model import CheckModel


class ExpensesModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    check_realtion = models.OneToOneField(CheckModel, on_delete=models.CASCADE, related_name="expenses")
    # discount_rate = models.FloatField(null=True, blank=True, default=0)
    # payment_date_discount = models.FloatField(null=True, blank=True, default=0)
    total_discounts = models.FloatField(null=True, blank=True, default=0)
    expenses = 250
    percentage = 15/100
