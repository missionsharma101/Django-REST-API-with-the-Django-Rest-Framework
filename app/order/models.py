from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Order(models.Model):
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    EXTRA_LARGE = 'extra-large'
    PENDING = 'pending'
    IN_TRANSIT = 'inTransit'
    DELIVERED = 'delivered'
    SIZES = [
        (SMALL, SMALL),
        (MEDIUM, MEDIUM),
        (LARGE, LARGE),
        (EXTRA_LARGE, EXTRA_LARGE)
    ]
    ORDER_STATUS = [
        (PENDING, PENDING),
        (IN_TRANSIT, IN_TRANSIT),
        (DELIVERED, DELIVERED)
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=20, choices=SIZES, default=SMALL)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS, default=PENDING)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Order {self.size} by {self.customer.id}>"
