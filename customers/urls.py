from django.urls import path

from . import views

app_name = 'customers'
urlpatterns = [
    path('create/', views.CreateCustomer.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateCustomer.as_view(), name='update'),
    path('car/', views.CreateCar.as_view(), name='create_car'),
]
