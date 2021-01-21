from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_enquiry/', views.add_enquiry, name='add_enquiry'),
]