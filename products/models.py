from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """ Category model """
    class Meta:
        """ use a verbose name"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ Product model """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    sku = models.CharField(
        max_length=254, null=True, blank=False, unique=True
        )
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    rating = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
        )
    likes = models.ManyToManyField(
        User,
        related_name='product_likes',
        blank=True
        )
    review_count = models.DecimalField(
        max_digits=6, decimal_places=0, null=True, blank=True, default=0
    )

    def __str__(self):
        return self.name
