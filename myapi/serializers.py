from rest_framework import serializers

from .models import Hero
from .models import Restaurant

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'yelp_id', 'name', 'phone', 'is_closed', 'review_count', 'yelp_rating', 'url', 'latitude', 'longitude', 'image_url', 'address', 'distance', 'tacoboutit_item_review_count')
