from django.urls import path
from app.views.checks_view import CheckReadCreateView, CheckReadUpdateDestroyView
from app.views.clients_view import ClientReadCreateView, ClientReadUpdateDestroyView
from app.views.expenses_view import ExpensesReadCreateView, ExpensesReadUpdateDestroyView


urlpatterns = [
    path("clients/", ClientReadCreateView.as_view(), name="clients"),
    path("clients/<pk>", ClientReadUpdateDestroyView.as_view(), name="read-update-destroy"),
    path("checks/", CheckReadCreateView.as_view(), name="checks"),
    path("checks/<pk>", CheckReadUpdateDestroyView.as_view(), name="read-update-destroy"),
    path("expenses/", ExpensesReadCreateView.as_view(), name="read-update-destroy"),
    path("expenses/<pk>", ExpensesReadUpdateDestroyView.as_view(), name="read-update-destroy"),
]
