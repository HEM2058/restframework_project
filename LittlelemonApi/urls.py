from django.urls import path
from .views import *

urlpatterns = [
   #   Menu-items endpoints
   path('menu-items',MenuItemView.as_view()),
   path('menu-items/<int:pk>',SingleMenuItemView.as_view()),
   
   # User group management endpoints
   path('groups/manager/users',UserView.as_view()),
   path('groups/manager/users/<int:pk>',SingleUserView.as_view()),

   # Cart management endpoints 
   path('cart/menu-items',CartView.as_view()),
   path('cart/menu-items/<int:pk>',SingleCartview.as_view()),

   # Order management endpoints
   path('orders/',OrdersView.as_view()),
   path('orders/<int:pk>',SingleOrdersView.as_view())

]
