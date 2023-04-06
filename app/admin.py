from django.contrib import admin  
from app.models.checks_model import CheckModel
from app.models.clients_model import ClientModel
from app.models.expenses_model import ExpensesModel
  
# Register your models here.  
admin.site.register(CheckModel)
admin.site.register(ClientModel)
admin.site.register(ExpensesModel)
