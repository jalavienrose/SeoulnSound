from django.db import models

class Shop(models.Model):
    application_name = models.CharField(max_length=255)
    self_name = models.CharField(max_length=255)
    pbp_class = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.TextField()