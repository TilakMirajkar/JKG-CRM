from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('item/create/', views.item_create, name='item_create'),
    path('item/<int:pk>/update/', views.item_update, name='item_update'),
    path('item/<int:pk>/delete/', views.item_delete, name='item_delete'),
    path('item/<int:item_id>/attributes/create/', views.item_attributes_create, name='item_attributes_create'),
    path('item/<int:item_id>/classification/create/', views.item_classification_create, name='item_classification_create'),
    path('item/<int:item_id>/location/create/', views.item_location_create, name='item_location_create'),
    path('item/<int:item_id>/tax/create/', views.item_tax_create, name='item_tax_create'),
    path('item/<int:item_id>/reorder/create/', views.item_reorder_create, name='item_reorder_create'),
    path('item/<int:item_id>/manufacturing/create/', views.item_manufacturing_create, name='item_manufacturing_create'),
    path('reports/', views.inventory_report, name='inventory_report'),
]