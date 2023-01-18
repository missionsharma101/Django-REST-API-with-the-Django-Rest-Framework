from rest_framework import serializers

from .models import Order
from ..authenticate.serilizer import UserCreationSerializers


class OrderSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    # mission = serializers.SerializerMethodField()
    order_status = serializers.HiddenField(default='PENDING')
    quantity = serializers.IntegerField()

    customer = UserCreationSerializers()

    class Meta:
        model = Order
        fields = ['id', 'size', 'order_status', 'quantity', 'customer']
        # depth = 1

    # def get_mission(self, obj):
    #     # import pdb;pdb.set_trace()
    #     a = {
    #         'a': "babu",
    #     }
    #     return a


class OrderDetailSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    order_status = serializers.CharField()
    quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Order
        fields = ['id''size', 'order_status', 'quantity', 'created_at', 'updated_at']
