import uuid

from django.db import models

from app.models.clients_model import ClientModel


class QuotationStatus(models.TextChoices):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    EXPIRED = "EXPIRED"


class CheckModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # client = models.ForeignKey(ClientModel, on_delete=models.CASCADE, db_constraint=False, related_name="checks")
    client_check_key = models.ForeignKey(ClientModel, on_delete=models.DO_NOTHING, related_name="client_check", blank=True, null=True)
    check_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    quotation_status = models.TextField(choices=QuotationStatus.choices, default=QuotationStatus.PENDING.value)
    amount_client_recieves = models.FloatField(null=True, blank=True)
    expiration_date = models.DateField()
