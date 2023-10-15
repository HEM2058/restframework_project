from django.urls import path
from .views import *

urlpatterns = [
   path('menu-items/',MenuItemView.as_view()),
   path('menu-items/<int:pk>',SingleMenuItemView.as_view()),
]
