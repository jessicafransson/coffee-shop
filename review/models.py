from django.db import models

from profiles.models import UserProfile
from products.models import Product

from profanity.validators import validate_is_profane


class Review(models.Model):
    """ A review model for users to review products """

    RATING = [
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING)
    body = models.TextField(max_length=1024, validators=[validate_is_profane])
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User: {self.user} rated {self.product}, {self.product} stars.'
