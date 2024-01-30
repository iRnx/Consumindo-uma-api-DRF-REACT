from django.urls import path

from . import views

app_name = 'custumers'

urlpatterns = [
    path('custumers/', views.CustumerListAPIView.as_view(), name='custumer-list')
]