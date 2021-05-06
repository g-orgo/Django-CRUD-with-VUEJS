from django.contrib import admin
from django.urls import path, include
from .routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base_files.urls')),
    path('api/', include(router.urls))
]
