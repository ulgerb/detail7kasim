
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appMy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('detail/', Detail),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
