from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import HeroSerializer
from .serializers import RestaurantSerializer

from .models import Hero
from .models import Restaurant
# Create your views here.

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class RestaurantViewSet(viewsets.ViewSet):
    # queryset = Restaurant.objects.all()
    # serializer_class = RestaurantSerializer

    # def get_queryset(self):
    #    restaurants = Restaurant.objects.all()
    #    return restaurants

    # Should this be a post request that redirects to get?
    def list(self, request):
        queryset = Restaurant.objects.all()
        serializer = RestaurantSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request):

        response = requests.get('https://api.yelp.com/v3/businesses/search?latitude=37.786882&longitude=-122.399972&limit=25', headers={'Authorization': 'Bearer 9thV13jtkqHq-k5tjfKPNvPk9jx8uU7I83PGIaWED9Ctv_YJOojIQ-VOsVB3POXnsX0nzNVjIAl41ynvS5pknNABaYlbTDfjwh4QHGn4m7PqXUA0mqcO9By2Jw34XXYx'})
        business_data = response.json()
        all_data_dicts = []
        data_dict = {}


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
            # return all_data_dicts
        for data in all_data_dicts:
            Restaurant.objects.create(**data)
        # print("test response", restaurant.yelp_id)
        # restaurants = self.get_queryset()
        # serializer = self.serializer_class()
        return HttpResponse('Restaurants Retrieved')


    # def get(request):
    #     response = requests.get('https://api.yelp.com/v3/businesses/search?latitude=37.786882&longitude=-122.399972&limit=25', headers={'Authorization': 'Bearer 9thV13jtkqHq-k5tjfKPNvPk9jx8uU7I83PGIaWED9Ctv_YJOojIQ-VOsVB3POXnsX0nzNVjIAl41ynvS5pknNABaYlbTDfjwh4QHGn4m7PqXUA0mqcO9By2Jw34XXYx'})
    #     business_data = response.json()
    #     all_data_dicts = []
    #     data_dict = {}
    #
    #
    #     for data in business_data['businesses']:
    #         data_dict = {}
    #         data_dict['yelp_id'] = data['id']
    #         data_dict['name'] = data['name']
    #         data_dict['phone'] = data['phone']
    #         data_dict['is_closed'] = data['is_closed']
    #         data_dict['review_count'] = data['review_count']
    #         data_dict['yelp_rating'] = data['rating']
    #         data_dict['url'] = data['url']
    #         data_dict['latitude'] = data['coordinates']['latitude']
    #         data_dict['longitude'] = data['coordinates']['longitude']
    #         data_dict['image_url'] = data['image_url']
    #         a = ", "
    #         data_dict['address'] = a.join(data['location']['display_address'])
    #         data_dict['distance'] = data['distance']
    #         all_data_dicts.append(data_dict)
    #         # return all_data_dicts
    #     for data in all_data_dicts:
    #         Restaurant.objects.create(**data)
    #     # print("test response", restaurant.yelp_id)
    #     # restaurants = self.get_queryset()
    #     # serializer = self.serializer_class()
    #     return HttpResponse(business_data['businesses'][0]['id'])
