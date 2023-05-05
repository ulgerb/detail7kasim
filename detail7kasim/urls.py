
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appMy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('detail/<id>/', detailPage, name='detailPage'),
    path('category/<cate>/', categoryPage, name='categoryPage'),
    path('category/<cate>/<group>/', categoryPage, name='categoryPageGroup'), 
    path('card-add/', cardAdd, name='cardAdd'),
    path('card-delete/<id>/', cardDelete, name='cardDelete'),
    
    # USER
    path('login/', loginUser, name='loginUser'),
    path('logout/', logoutUser, name='logoutUser'),
    path('register/', registerUser, name='registerUser'),
    path('profile/', profileUser, name='profileUser'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
