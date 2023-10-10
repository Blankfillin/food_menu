from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="",
    )

    def __str__(self) -> str:
        return self.item_name

    added_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
