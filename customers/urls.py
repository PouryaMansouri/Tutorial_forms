from django.urls import path

from . import views

app_name = 'customers'
urlpatterns = [
    path('c-create/', views.CreateCustomer.as_view(), name='create'),
]
