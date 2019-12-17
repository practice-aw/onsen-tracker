from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=60)
    yelp_id = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    is_closed = models.BooleanField(default=True)
    review_count = models.IntegerField()
    url = models.CharField(max_length=60)
    latitude = models.FloatField(max_length=100)
    longitude = models.FloatField(max_length=100)
    image_url = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    distance = models.FloatField(max_length=100)
    # transactions = ArrayField(models.CharField(max_length=50), blank=True)
    tacoboutit_item_review_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
