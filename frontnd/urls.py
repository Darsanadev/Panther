from django.urls import path
from . import views

app_name = 'frontnd'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.home, name='index'),
    path('contact/', views.contact, name='contact'),
    
    ]
