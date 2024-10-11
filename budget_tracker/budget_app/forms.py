from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'category', 'description', 'amount', 'date']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'date'}),
        }
