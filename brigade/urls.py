
from django.contrib import admin
from django.urls import path, include
from frontnd import views  # Assuming your views are in the 'frontnd' app
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('frontnd.urls')),

]

# Serve static files in development only
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

    # Serve media files in development only
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
