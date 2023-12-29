from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('admins.urls')),
    path('api/', include('users.urls')),
    path('api/', include('clients.urls')),
    path('api/', include('admins.urls')),
    path('api/', include('schedules.urls')),
    path('api/', include('finances.urls')),
]
