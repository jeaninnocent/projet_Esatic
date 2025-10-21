from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('concours/', views.concours, name='concours'),
    path('contact/', views.contact, name='contact'),
    path('inscription/', views.inscription, name='inscription'),
]
