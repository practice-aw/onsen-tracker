from rest_framework import serializers

from .models import Hero
from .models import Restaurant, Taco

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')

class TacoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taco
        # this might need to be changed
        fields = "__all__"

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    # consider adding this tacos = TacoSerializer(many=True, read_only=True)
    class Meta:
        model = Restaurant
        fields = ('id', 'yelp_id', 'name', 'phone', 'is_closed', 'review_count', 'yelp_rating', 'url', 'latitude', 'longitude', 'image_url', 'address', 'distance', 'tacoboutit_item_review_count')
        # add tacos to fields
