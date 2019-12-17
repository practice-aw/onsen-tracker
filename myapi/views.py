from django.shortcuts import render
from django.http import HttpResponse
import requests

from rest_framework import viewsets

from .serializers import HeroSerializer
from .serializers import RestaurantSerializer

from .models import Hero
from .models import Restaurant
# Create your views here.

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

def home(request):
    response = requests.get('https://api.yelp.com/v3/businesses/search?latitude=37.786882&longitude=-122.399972', headers={'Authorization': 'Bearer 9thV13jtkqHq-k5tjfKPNvPk9jx8uU7I83PGIaWED9Ctv_YJOojIQ-VOsVB3POXnsX0nzNVjIAl41ynvS5pknNABaYlbTDfjwh4QHGn4m7PqXUA0mqcO9By2Jw34XXYx'})
    business_data = response.json()
    name = business_data['businesses'][0]['alias']
    yelp_id = business_data['businesses'][0]['id']
    restaurant = Restaurant.objects.create(name=name, yelp_id=yelp_id)
    print("test response", restaurant.yelp_id)
    return HttpResponse(business_data['businesses'][0]['id'])
