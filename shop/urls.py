from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('affiliate/', include('affiliate.urls')),
    path('api_basic/', include('api_basic.urls')),
    path('PF2/', include('PF2.urls')),
]
