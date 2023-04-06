from rest_framework import generics

from app.models.clients_model import ClientModel

from app.serializers.clients_serializer import ClientModelSerializer


class ClientReadCreateView(generics.ListCreateAPIView):
    queryset = ClientModel.objects.all()
    serializer_class = ClientModelSerializer

class ClientReadUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):    
    queryset = ClientModel.objects.all()    
    serializer_class = ClientModelSerializer
