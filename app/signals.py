from datetime import datetime

from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.models.checks_model import CheckModel
from app.models.expenses_model import ExpensesModel


@receiver(post_save, sender=CheckModel)
def calculate_amount_client_recieves(sender, instance: CheckModel, created, **kwargs):
    if created:
        expenses = ExpensesModel.objects.create(check_relation = instance)
        
        days_difference = (instance.expiration_date - datetime.now().date()).days

        expenses.total_discounts = instance.check_amount * expenses.percentage * ( days_difference / 365 ) + expenses.expenses

        instance.amount_client_recieves = instance.check_amount - expenses.total_discounts
        
        instance.save()
        expenses.save()
