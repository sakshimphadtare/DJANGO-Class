from django.db import models
from django.utils import timezone
from django.db import models

class Transaction(models.Model):
    # Choices for transaction type
    INCOME = 'Income'
    EXPENSE = 'Expense'
    TYPE_CHOICES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    ]

    # Choices for transaction category
    CATEGORY_CHOICES = [
        ('Income', 'Income'),
        ('Rent', 'Rent'),
        ('Food', 'Food'),
        ('Utilities', 'Utilities'),
        ('Entertainment', 'Entertainment'),
        ('Others', 'Others'),
    ]

    # Transaction fields
    transaction_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.description}: {self.amount} ({self.transaction_type})"

class Budget(models.Model):
    name = models.CharField(max_length=255)
    amount = models.FloatField()
    # Add any other fields you need

    def __str__(self):
        return self.name
