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

    # def __init__(self, data):
    #     self.name = data['businesses'][0]['alias']
        # self.yelp_id = data['businesses'][0]['id']

    def __str__(self):
        return self.name
