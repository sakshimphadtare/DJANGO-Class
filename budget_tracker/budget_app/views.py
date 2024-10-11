from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import TransactionForm
from rest_framework import generics
from .models import budget
from .serializers import BudgetSerializer

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'budget_app/transaction_list.html', {'transactions': transactions})

def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'budget_app/transaction_form.html', {'form': form})

def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'budget_app/transaction_form.html', {'form': form})

def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'budget_app/transaction_confirm_delete.html', {'transaction': transaction})


class BudgetListCreateView(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

class BudgetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

