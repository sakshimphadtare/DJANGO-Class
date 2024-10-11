from django.urls import path
from . import views
from .views import BudgetListCreateView, BudgetDetailView, TransactionListCreateView, TransactionDetailView

urlpatterns = [
    # Root URL that redirects to the transaction list
    path('', views.transaction_list, name='transaction_list'),  # This will handle requests to /

    # Function-based views for transactions
    path('new/', views.transaction_create, name='transaction_create'),
    path('<int:pk>/edit/', views.transaction_update, name='transaction_update'),
    path('<int:pk>/delete/', views.transaction_delete, name='transaction_delete'),

    # API views for budgets
    path('budgets/', BudgetListCreateView.as_view(), name='budget-list-create'),
    path('budgets/<int:pk>/', BudgetDetailView.as_view(), name='budget-detail'),

    # API views for transactions - adjusted to remove the redundant 'api' prefix
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
]
