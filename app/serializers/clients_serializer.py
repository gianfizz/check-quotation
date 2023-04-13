from rest_framework import serializers

from app.models.clients_model import ClientModel
from app.serializers.checks_serializer import CheckModelSerializer

class ClientModelSerializer(serializers.ModelSerializer):
    checks = CheckModelSerializer(many=True, read_only=True)
    class Meta:
        model = ClientModel
        fields = [
            "uuid", "full_name", "cuit_or_ruc", "email", "phone", "client_check"
            ]
