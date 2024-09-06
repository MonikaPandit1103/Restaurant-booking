from django.shortcuts import render
from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.permissions import IsAuthenticated

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

# Create your views here.
from django.shortcuts import render
from .models import Customer

def customer_list_view(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})
