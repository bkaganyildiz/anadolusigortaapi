# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from anadolucore.models import Customer
from anadolucore.serializers import CustomerSerializer

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    authentication_classes = [IsAuthenticated]

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [IsAuthenticated]