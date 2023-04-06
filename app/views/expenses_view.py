from rest_framework import generics

from app.models.expenses_model import ExpensesModel

from app.serializers.expenses_serializer import ExpensesModelSerializer


class ExpensesReadCreateView(generics.ListCreateAPIView):
    queryset = ExpensesModel.objects.all()
    serializer_class = ExpensesModelSerializer

class ExpensesReadUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):    
    queryset = ExpensesModel.objects.all()    
    serializer_class = ExpensesModelSerializer
