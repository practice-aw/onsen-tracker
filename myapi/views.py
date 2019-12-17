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
    response = requests.get('https://api.yelp.com/v3/businesses/search?latitude=37.786882&longitude=-122.399972&limit=25', headers={'Authorization': 'Bearer 9thV13jtkqHq-k5tjfKPNvPk9jx8uU7I83PGIaWED9Ctv_YJOojIQ-VOsVB3POXnsX0nzNVjIAl41ynvS5pknNABaYlbTDfjwh4QHGn4m7PqXUA0mqcO9By2Jw34XXYx'})
    business_data = response.json()
    data_dict = {}
    data_dict['yelp_id'] = business_data['businesses'][0]['id']
    data_dict['name'] = business_data['businesses'][0]['name']
    data_dict['phone'] = business_data['businesses'][0]['phone']
    data_dict['is_closed'] = business_data['businesses'][0]['is_closed']
    data_dict['review_count'] = business_data['businesses'][0]['review_count']
    data_dict['url'] = business_data['businesses'][0]['url']
    data_dict['latitude'] = business_data['businesses'][0]['coordinates']['latitude']
    data_dict['longitude'] = business_data['businesses'][0]['coordinates']['longitude']
    data_dict['image_url'] = business_data['businesses'][0]['image_url']
    a = ", "
    data_dict['address'] = a.join(business_data['businesses'][0]['location']['display_address'])
    data_dict['distance'] = business_data['businesses'][0]['distance']
    # data_dict['transactions'] = business_data['businesses'][0]['transactions']
    restaurant = Restaurant(**data_dict)
    restaurant.save()
    # restaurant = Restaurant.objects.create(data_dict)
    print("test response", restaurant.yelp_id)
    return HttpResponse(business_data['businesses'][0]['id'])
