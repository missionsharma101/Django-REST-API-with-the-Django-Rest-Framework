from django.urls import path

from app.order.views import *

urlpatterns = [
    path('', GetOrderView.as_view(), name="auth"),
    path('createView', OrderCreateView.as_view(), name="createView"),
    path('DetailView/<int:order_id>', OrderDetailView.as_view(), name="DetailView"),
    path('OrderView/', UserOrderView.as_view(), name="OrderView"),
    path('user/<int:user_id>/order/<int:order_id>', UserOrderDetail.as_view(), name="user_detail")

]
