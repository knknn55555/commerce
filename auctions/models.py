from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class auction_list(models.Model):
    auction_image = models.ImageField(blank=True, null=True)
    auction_title = models.CharField(max_length=64)
    auction_price = models.IntegerField(blank=True, null=True)
    auction_description = models.TextField(max_length=255, blank=True, null=True)
    created_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    def __str__(self):
        return f'{self.auction_title}'