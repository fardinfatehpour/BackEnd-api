from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.item_list, name='item_list'),
    path('add/', views.item_add, name='item_add'),
    path('delete/', views.item_delete, name='item_delete'),
    path('edit/', views.item_edit, name='item_edit'),
]
