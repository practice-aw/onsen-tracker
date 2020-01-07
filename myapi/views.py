from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests, json

from django.views.decorators.csrf import csrf_exempt
from .utils import data_org
from decouple import config

from rest_framework import viewsets, mixins, generics, status
from rest_framework.response import Response

from .serializers import RestaurantSerializer, TacoSerializer, ReviewSerializer

from .models import Taco, Review, Restaurant
# Create your views here.

class TacoViewSet( mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Taco.objects.all()
    serializer_class = TacoSerializer

    @csrf_exempt
    def post_new(request):
        data = request.POST
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        id = body['restaurant']
        restaurant = Restaurant.objects.filter(id=id)
        if(restaurant and 'type' in body):
            taco = Taco.objects.get_or_create(
                restaurant_id = id,
                type = body['type']
            )
            if(taco[1]):
                content = {
                     'success': f'{taco[0]} added to {restaurant[0]}'
                  }
                return JsonResponse(content, status=status.HTTP_201_CREATED)
            else:
                content = {
                     'error': f'{taco[0]} already exists'
                  }
                return JsonResponse(content, status=status.HTTP_226_IM_USED)
        else:
             content = {
                  'error': f'A restaurant with id: {id} does not exist'
               }
             return JsonResponse(content, status=status.HTTP_404_NOT_FOUND)



class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantUpdateOrCreateViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def retrieve(request):
        params = request.GET
        # lng = params['lng']

        if('lat' and 'lng' in params):
            lat = params['lat']
            lng = params['lng']
            YELP_API_KEY = config('YELP_API_KEY')

            response = requests.get(f'https://api.yelp.com/v3/businesses/search?latitude={lat}&longitude={lng}&limit=5&categories=mexican,tacos', headers={'Authorization': YELP_API_KEY})
            business_data = response.json()
            all_data_dicts = []
            yelp_ids = []
            if(business_data['total'] != 0):
                data_org(business_data, all_data_dicts, yelp_ids)

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
        else:
            content = {
              'error': 'Please Provide a latitude and longitude'
          }
        return JsonResponse(content, status=status.HTTP_400_BAD_REQUEST)
