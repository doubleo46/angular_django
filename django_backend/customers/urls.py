"""Urls of customers data."""
from .views import CreateCustomer, CustomersView
from rest_framework.routers import SimpleRouter
from django.urls import path

urlpatterns = [
    path('customers', CustomersView.as_view(), name='customers')
]

router = SimpleRouter(trailing_slash=False)
router.register(r'create_customer', CreateCustomer, "CreateCustomer")

urlpatterns += router.urls
