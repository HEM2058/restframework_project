from django.shortcuts import render
from rest_framework import generics
from .serializers import CategorySerializer, MenuItemSerializer, CartSerializer,OrderSerializer ,OrderItemSerializer
from .models import *
from django.contrib.auth.models import User, Group
from .permissions import ReadOnlyOrUnauthorized
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# Create your views here.

@permission_classes([IsAuthenticated])
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [ReadOnlyOrUnauthorized]


@permission_classes([IsAuthenticated])
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.RetrieveDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [ReadOnlyOrUnauthorized]