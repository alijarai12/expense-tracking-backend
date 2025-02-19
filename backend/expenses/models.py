from django.db import models

class Expense(models.Model):
    expense_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category_name = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.expense_name
