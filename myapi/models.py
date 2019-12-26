from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=400)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=400)
    yelp_id = models.CharField(max_length=400)
    phone = models.CharField(max_length=400, null=True)
    is_closed = models.BooleanField(null=True)
    review_count = models.IntegerField(default=0)
    yelp_rating = models.FloatField(default=0)
    url = models.CharField(max_length=400, null=True)
    latitude = models.FloatField(max_length=100, null=True)
    longitude = models.FloatField(max_length=100, null=True)
    image_url = models.CharField(max_length=400, null=True)
    address = models.CharField(max_length=100, null=True)
    distance = models.FloatField(max_length=100, null=True)
    # transactions = ArrayField(models.CharField(max_length=50), blank=True)
    tacoboutit_item_review_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Taco(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="tacos")
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type
