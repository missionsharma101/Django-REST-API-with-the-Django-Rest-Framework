from django.urls import  path

from app.order.views import GetOrderView

urlpatterns = [
    path('', GetOrderView.as_view(), name="auth"),

]
