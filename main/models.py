import uuid
from django.db import models

class Shop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.TextField()