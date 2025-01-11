
from django.contrib import admin
from django.urls import path, include
from frontnd import views  # Assuming your views are in the 'frontnd' app

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('frontnd.urls')),
]
