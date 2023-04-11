from datetime import datetime

from app.models.checks_model import CheckModel
from app.models.expenses_model import ExpensesModel


class CheckServices:
    @staticmethod
    def quotate_check(uuid: str):
        check_model = CheckModel.objects.filter(uuid=uuid)
        expenses = ExpensesModel.objects.filter(check_realtion=check_model)

        #calculate difference in days between today and check pay day
        days_difference = (check_model.expiration_date - datetime.now().date()).days

        #calculate the discount on the check
        expenses.total_discounts = check_model.check_amount * expenses.percentage * (days_difference / 365) - expenses.expenses

        #calculate what the client recieves
        check_model.amount_client_recieves = check_model.check_amount - expenses.total_discounts
        
        check_model.save()
        expenses.save()
