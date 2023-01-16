from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include('app.authenticate.urls')),
    path("order/", include('app.order.urls'))
]
