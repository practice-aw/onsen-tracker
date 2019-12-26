from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests

from decouple import config

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .serializers import HeroSerializer
from .serializers import RestaurantSerializer, TacoSerializer

from .models import Hero, Taco
from .models import Restaurant
# Create your views here.

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class TacoViewSet(viewsets.ModelViewSet):
    queryset = Taco.objects.all()
    serializer_class = TacoSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantUpdateOrCreateViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def retrieve(request):
        print("you hit the retrieve route")
        params = request.GET
        lat = params['lat']
        lng = params['lng']
        YELP_API_KEY = config('YELP_API_KEY')

        response = requests.get(f'https://api.yelp.com/v3/businesses/search?latitude={lat}&longitude={lng}&limit=5&categories=mexican,tacos', headers={'Authorization': YELP_API_KEY})
        business_data = response.json()
        all_data_dicts = []
        yelp_ids = []
        data_dict = {}
        if(business_data['total'] != 0):
            for data in business_data['businesses']:
                data_dict = {}
                data_dict['yelp_id'] = data['id']
                data_dict['name'] = data['name']
                data_dict['phone'] = data['phone']
                data_dict['is_closed'] = data['is_closed']
                data_dict['review_count'] = data['review_count']
                data_dict['yelp_rating'] = data['rating']
                data_dict['url'] = data['url']
                data_dict['latitude'] = data['coordinates']['latitude']
                data_dict['longitude'] = data['coordinates']['longitude']
                data_dict['image_url'] = data['image_url']
                a = ", "
                data_dict['address'] = a.join(data['location']['display_address'])
                data_dict['distance'] = data['distance']
                all_data_dicts.append(data_dict)
                yelp_ids.append(data['id'])
            for data in all_data_dicts:
                Restaurant.objects.update_or_create(
                    yelp_id = data['yelp_id'],
                    defaults={'name': data['name'], 'phone': data['phone'], 'is_closed': data['is_closed'],
                    'review_count': data['review_count'], 'yelp_rating': data['yelp_rating'], 'url': data['url'],
                    'latitude': data['latitude'], 'longitude': data['longitude'], 'image_url': data['image_url'],
                    'address': data['address'], 'distance': data['distance']},
                )
            queryset = Restaurant.objects.filter(yelp_id__in=yelp_ids)
            serializer = RestaurantSerializer(queryset, many=True)

            return JsonResponse(serializer.data, safe=False)
        else:
              content = {
                'status': 'Resource Not Found'
            }
        return JsonResponse(content, status=status.HTTP_404_NOT_FOUND)
