from django.urls import path
from . import views

app_name = 'frontnd'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('index/', views.home, name='index'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('res/', views.res, name='res'),
    path('gallary/', views.gallary, name='gallary'),

# function(e,t){"use strict"
]
