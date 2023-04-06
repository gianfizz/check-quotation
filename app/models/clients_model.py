import uuid

from django.db import models


class ClientModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.TextField(max_length=64)
    cuit_or_ruc = models.TextField(max_length=15)
    email = models.TextField(max_length=64)
    phone = models.TextField(max_length=64)
