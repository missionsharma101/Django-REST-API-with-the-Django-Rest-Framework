from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import serilizer
from .models import Order


class GetOrderView(generics.GenericAPIView):

    def get(self, request):
        return Response(data="hello order")


class OrderCreateView(generics.GenericAPIView):
    serializer_class = serilizer.OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.all()
        serializers = self.serializer_class(instance=orders, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        user = request.user
        if serializers.is_valid():
            serializers.save(customer=user)
            return Response(data=serializers.data, status=status.HTTP_200_OK)
        return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(generics.GenericAPIView):
    serializer_class = serilizer.OrderSerializer
    permission_classes = [IsAuthenticated]

    # queryset = Order.objects.get(id)
    def get(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        serilizers = self.serializer_class(instance=order)
        return Response(data=serilizers.data, status=status.HTTP_200_OK)

    def put(self, request, order_id):
        pass
