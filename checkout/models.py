import uuid

from decimal import Decimal
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile
from coupons.models import Coupon


class Order(models.Model):
    # the orders will not be automatically generated
    # we want them unique and permanent so users can find previous
    order_number = models.CharField(
        max_length=32, null=False, editable=False
    )
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='orders'
    )
    full_name = models.CharField(
        max_length=50, null=False, blank=False
    )
    email = models.EmailField(
        max_length=254, null=False, blank=False
    )
    phone_number = models.CharField(
        max_length=20, null=False, blank=False
    )
    country = CountryField(
        blank_label='Country *', null=False, blank=False
    )
    postcode = models.CharField(
        max_length=20, null=True, blank=True
    )
    town_or_city = models.CharField(
        max_length=40, null=False, blank=False
    )
    street_address1 = models.CharField(
        max_length=80, null=False, blank=False
    )
    street_address2 = models.CharField(
        max_length=80, null=True, blank=True
    )
    county = models.CharField(
        max_length=80, null=True, blank=True
    )
    # this one automatically sets date and time
    # for when the order is created
    date = models.DateTimeField(
        auto_now_add=True
    )
    first_order = models.BooleanField(
        default=False
    )
    coupon = models.ForeignKey(
        Coupon, related_name='orders',
        null=True, blank=True, on_delete=models.SET_NULL
    )
    # these three fields are calculated with model method
    # every time an order is saved
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
        )
    discount = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    order_subtotal = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
        )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
        )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
        )
    original_bag = models.TextField(
        null=False,
        blank=False,
        default=''
    )
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default=''
    )

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        if self.discount == 0:
            self.order_total = self.lineitems.aggregate(
                Sum('lineitem_total')
                )['lineitem_total__sum'] or 0
        else:
            discount_as_decimal = Decimal(self.discount / 100)
            total = self.lineitems.aggregate(
                Sum('lineitem_total')
                )['lineitem_total__sum'] or 0
            self.order_subtotal = total
            discount = total * discount_as_decimal
            self.order_total = total - discount

        quantity = self.lineitems.aggregate(
            Sum('quantity')
            )['quantity__sum'] or 0

        if self.first_order is True:
            self.delivery_cost = 0
        elif self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = settings.STANDARD_DELIVERY_PERCENTAGE
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
        )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
        )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
        )

    def save(self, *args, **kwargs):
        """
        overrides the original save method to set order number,
        if it hasn't already been set
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
