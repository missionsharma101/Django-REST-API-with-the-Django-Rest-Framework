from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    order_status = serializers.HiddenField(default='PENDING')
    quantity = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ['size', 'order_status', 'quantity']
