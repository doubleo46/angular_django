"""Urls of customers data."""
from .views import CreateCustomer, CustomersView, CustomerCreate, CustomerUpdate, CustomerDelete
from rest_framework.routers import SimpleRouter
from django.urls import path

urlpatterns = [
    path('customers', CustomersView.as_view(), name='customers'),
    path('customer/add/', CustomerCreate.as_view(), name='customer-add'),
    path('customer/<int:pk>/', CustomerUpdate.as_view(), name='customer-update'),
    path('customer/<int:pk>/delete', CustomerDelete.as_view(), name='customer-delete'),
]

router = SimpleRouter(trailing_slash=False)
router.register(r'create_customer', CreateCustomer, "CreateCustomer")

urlpatterns += router.urls
