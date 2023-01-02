
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('dress/', include('dress.urls')),
    path('hijab/', include('hijab.urls')),
    path('blouse/',include ('blouse.urls')),
]
