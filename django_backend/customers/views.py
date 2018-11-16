from rest_framework.response import Response
from rest_framework import permissions, viewsets
from rest_framework.decorators import permission_classes

from .models import Customers
# Create your views here.


@permission_classes((permissions.AllowAny,))
class CreateCustomer(viewsets.ViewSet):
    """API to create customers."""

    def create(self, request):
        """Save customer data from post."""
        print(request.data)
        Customers.objects.create(name=request.data['name'],age=request.data['age'])
        return Response({"st": 200})
