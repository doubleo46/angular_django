"""Urls of customers data."""
from .views import CreateCustomer
from rest_framework.routers import SimpleRouter


urlpatterns = [
]

router = SimpleRouter(trailing_slash=False)
router.register(r'create_customer', CreateCustomer, "CreateCustomer")

urlpatterns += router.urls
