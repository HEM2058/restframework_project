from django.shortcuts import render
from rest_framework import generics
from .serializers import CategorySerializer, MenuItemSerializer, CartSerializer,OrderSerializer ,OrderItemSerializer
from .models import *
from django.contrib.auth.models import User, Group
from .permissions import ReadOnlyOrUnauthorized
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# Create your views here.


class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrUnauthorized]


class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.RetrieveDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrUnauthorized]