from django.urls import path

from app.order.views import *

urlpatterns = [
    path('', GetOrderView.as_view(), name="auth"),
    path('createView', OrderCreateView.as_view(), name="createView"),
    path('DetailView/<int:order_id>', OrderDetailView.as_view(), name="DetailView")


]
