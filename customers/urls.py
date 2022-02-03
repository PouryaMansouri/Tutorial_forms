from django.urls import path

from . import views

app_name = 'customers'
urlpatterns = [
    path('create/', views.CreateCustomer.as_view(), name='create'),
]
