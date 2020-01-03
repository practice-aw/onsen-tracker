from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg

# Create your models here.

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

    #  Properties allow us to call self.tacos()
    # @property
    # def tacos(self):
    #     return self.tacos.all()

class Taco(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="tacos")
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

    # @property
    # def reviews(self):
    #     print("testing testing")
    #     return self.reviews.all()

    @property
    def average_rating(self):
        print("testing testing", self.reviews.aggregate(Avg('rating'))['rating__avg'])
        # return self.reviews
        return self.reviews.aggregate(Avg('rating'))['rating__avg']

class Review(models.Model):
    taco = models.ForeignKey(Taco, on_delete=models.CASCADE, related_name="reviews")
    rating = models.FloatField(default=10, validators=[MinValueValidator(1), MaxValueValidator(10)])
    review = models.TextField(max_length=900, null=True, blank=True)
    def __str__(self):
        return self.rating
