from django.urls import path
from .views import *

urlpatterns = [
   #   Menu-items endpoints
   path('menu-items',MenuItemView.as_view()),
   path('menu-items/<int:pk>',SingleMenuItemView.as_view()),
   
   # User group management endpoints
   path('groups/manager/users',UserView.as_view()),
   path('groups/manager/users/<int:pk>',SingleUserView.as_view()),
]
