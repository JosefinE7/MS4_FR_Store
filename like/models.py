from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class LikeProducts(models.Model):

    class Meta:
        verbose_name_plural = 'Likes'

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_like')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_like')
    like = models.SmallIntegerField()

    def __str__(self):
        return self.user.username
