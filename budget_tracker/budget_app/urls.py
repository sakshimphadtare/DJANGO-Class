from django.urls import path
from . import views
from .views import BudgetListCreateView, BudgetDetailView

urlpatterns = [
    path('', views.transaction_list, name='transaction_list'),
    path('new/', views.transaction_create, name='transaction_create'),
    path('<int:pk>/edit/', views.transaction_update, name='transaction_update'),
    path('<int:pk>/delete/', views.transaction_delete, name='transaction_delete'),
    path('budgets/', BudgetListCreateView.as_view(), name='budget-list-create'),
    path('budgets/<int:pk>/', BudgetDetailView.as_view(), name='budget-detail'),

]


