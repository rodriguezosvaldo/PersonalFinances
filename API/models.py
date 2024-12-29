from django.db import models

# Create your models here.
class AmountType(models.Model):
    AMOUNT_TYPE_CHOICES = [
        ('fixed_expense', 'Fixed Expense'),
        ('variable_expense', 'Variable Expense'),
        ('fixed_income', 'Fixed Income'),
        ('variable_income', 'Variable Income'),
    ]
    type = models.CharField(max_length=100, choices=AMOUNT_TYPE_CHOICES)
    class Meta:
        db_table = 'amount_type'

class AccountType(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('card', 'Card'),
        ('cash', 'Cash'),
        ('savings', 'Savings'),
        ('investment', 'Investment'),
    ]
    type = models.CharField(max_length=100, choices=ACCOUNT_TYPE_CHOICES)
    class Meta:
        db_table = 'account_type'

class Accounts(models.Model):
    account = models.CharField(max_length=100)
    type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'accounts'

class Categories(models.Model):
    category = models.CharField(max_length=100)
    class Meta:
        db_table = 'categories'

class Transactions(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_type = models.ForeignKey(AmountType, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    class Meta:
        db_table = 'transactions'