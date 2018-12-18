from rest_framework.response import Response
from rest_framework import permissions, viewsets
from rest_framework.decorators import permission_classes

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Customers
from .forms import CustomerForm


@permission_classes((permissions.AllowAny,))
class CreateCustomer(viewsets.ViewSet):
    """API to create customers."""

    def create(self, request):
        """Save customer data from post."""
        print(request.data)
        Customers.objects.create(
            name=request.data['name'], age=request.data['age'])
        return Response({"st": 200})


class CustomersView(ListView):
    """List active customers."""
    queryset = Customers.objects.filter(is_active=True)
    template_name = 'customers/customers_list.html'


class CustomerCreate(CreateView):
    model = Customers
    fields = ['name', 'age']
    template_name = 'customers/customer_form.html'
    success_url = reverse_lazy('customers')


class CustomerUpdate(UpdateView):
    model = Customers
    fields = ['name', 'age']
    template_name = 'customers/customer_form.html'
    success_url = reverse_lazy('customers')


class CustomerDelete(DeleteView):
    model = Customers
    success_url = reverse_lazy('customers')
