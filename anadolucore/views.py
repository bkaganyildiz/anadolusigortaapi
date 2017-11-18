# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

import django_filters
# Create your views here.
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from anadolucore.choices import L0, L1, L2, L3, L4
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
def replace_underscore_with_whitespaces(tuples):
    sorted_by_first = map(lambda x: (int(x[0]), x[1].replace('_', ' ')), tuples)
    sorted_by_first = sorted(sorted_by_first, key=lambda tuples: tuples[0])
    return sorted_by_first

@api_view(['GET'])
def LList(request):
    l_map = []
    l_map.append(replace_underscore_with_whitespaces(L0.choices()))
    l_map.append(replace_underscore_with_whitespaces(L1.choices()))
    l_map.append(replace_underscore_with_whitespaces(L2.choices()))
    l_map.append(replace_underscore_with_whitespaces(L3.choices()))
    l_map.append(replace_underscore_with_whitespaces(L4.choices()))
    return HttpResponse(content= json.dumps(l_map))
@api_view(['GET'])
def L1List(request):
    return HttpResponse(content= json.dumps(L1.choices()))
@api_view(['GET'])
def L2List(request):
    return HttpResponse(content= json.dumps(L2.choices()))
@api_view(['GET'])
def L0List(request):
    return HttpResponse(content= json.dumps(L0.choices()))
@api_view(['GET'])
def L3List(request):
    return HttpResponse(content= json.dumps(L3.choices()))
@api_view(['GET'])
def L4List(request):
    return HttpResponse(content= json.dumps(L4.choices()))