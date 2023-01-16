from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Customers, Products
from api.serializer import CustomerSerializers, ProductSerializers


# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializers


    @action(detail=True , methods=['get'])
    def products(self,request, pk=None):
        try:
            customer = Customers.objects.get(pk=pk)
            prod = Products.objects.filter(customer=customer)
            prods_serializer = ProductSerializers(prod,many=True, context={'request':request})
            return Response(prods_serializer.data)
        except Exception as e:
            return Response({
                'message': "company is not availabe"
            })



class ProductViewSet(viewsets.ModelViewSet):
        queryset = Products.objects.all()
        serializer_class = ProductSerializers










