from rest_framework import generics

from app.models.checks_model import CheckModel
from app.serializers.checks_serializer import CheckModelSerializer


class CheckReadCreateView(generics.ListCreateAPIView):
    queryset = CheckModel.objects.all()
    serializer_class = CheckModelSerializer

class CheckReadUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):    
    queryset = CheckModel.objects.all()    
    serializer_class = CheckModelSerializer
