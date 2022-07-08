import imp
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard'),
    path('customers-info/<int:pk>/', views.customers, name='customers'),
    path('products-details/', views.products, name='products' ),
    path('create_order/', views.create_order, name='create_order'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.deleteOrder, name='delete')
]
