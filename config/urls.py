from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include('app.authenticate.urls')),
    path("orders/", include('app.order.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
