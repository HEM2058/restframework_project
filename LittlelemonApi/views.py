from django.shortcuts import render
from rest_framework import generics
from .serializers import CategorySerializer, MenuItemSerializer, CartSerializer,OrderSerializer ,OrderItemSerializer, UserSerializer, GroupSerializer
from .models import *
from django.contrib.auth.models import User, Group
from .permissions import ReadOnlyOrUnauthorized
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# Create your views here.

#  Menu-items endpoints views

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrUnauthorized]


class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.RetrieveDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrUnauthorized]


# User group management endpoints views
class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrUnauthorized]

    def get_queryset(self):
        # Filter users who are in the 'Manager' group
        return User.objects.filter(groups__name='Manager')
     


class SingleUserView(generics.RetrieveUpdateAPIView,generics.RetrieveDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrUnauthorized]

    def get_queryset(self):
        # Filter users who are in the 'Manager' group
        return User.objects.filter(groups__name='Manager')
    
# Cart management endpoints views

class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrUnauthorized]


class SingleCartview(generics.RetrieveUpdateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrUnauthorized]
    
# Order management endpoints views

class OrdersView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class =OrderSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrUnauthorized]

class SingleOrdersView(generics.RetrieveUpdateAPIView,generics.RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class =OrderSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrUnauthorized]