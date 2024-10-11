# serializers.py

from rest_framework import serializers
from .models import Budget

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'  # You can also list specific fields like ['id', 'name', 'amount', 'date']
