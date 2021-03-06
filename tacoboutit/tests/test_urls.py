
import json, requests
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from decouple import config
from django.utils.html import escape
from myapi.models import Restaurant, Taco, Review, User


class RestaurantTestCase(APITestCase):
    def setUp(self):
        restuarant = Restaurant.objects.create(name='scotts tacos',
                        yelp_id = "akbkhadfb",
                        phone = "123456789",
                        is_closed = False,
                        review_count = 10,
                        yelp_rating = 4.7,
                        url = "http.hfhsf",
                        latitude = 47.60934,
                        longitude = -122.34076,
                        image_url = "https://s3-media3.fl.yelpcdn.com/bphoto/LFo_pxrIEmbVhkKSzZ0jiA/o.jpg",
                        address = "1521 1st Ave, Seattle, WA 98101",
                        distance = 100.7,
                        tacoboutit_item_review_count = 0)
        # print(restuarant.id)
        taco = Taco.objects.create(type='al pastor test taco', restaurant_id=restuarant.id)

    def test_get_all_restaurants(self):
        taco_id = Taco.objects.get(type='al pastor test taco').id
        response = self.client.get('/api/v1/restaurants/')

        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'scotts tacos')
        self.assertEqual(response.data[0]['yelp_id'], 'akbkhadfb')
        self.assertEqual(response.data[0]['phone'], '123456789')
        self.assertEqual(response.data[0]['is_closed'], False)
        self.assertEqual(response.data[0]['review_count'], 10)
        self.assertEqual(response.data[0]['yelp_rating'], 4.7)
        self.assertEqual(response.data[0]['tacos'][0]['id'], taco_id)

    def test_get_one_restaurant(self):
        taco_id = Taco.objects.get(type='al pastor test taco').id
        restaurant_id = Restaurant.objects.get(name='scotts tacos').id
        response = self.client.get(f'/api/v1/restaurants/{restaurant_id}/')

        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'scotts tacos')
        self.assertEqual(response.data['yelp_id'], 'akbkhadfb')
        self.assertEqual(response.data['phone'], '123456789')
        self.assertEqual(response.data['is_closed'], False)
        self.assertEqual(response.data['review_count'], 10)
        self.assertEqual(response.data['yelp_rating'], 4.7)
        self.assertEqual(response.data['tacos'][0]['id'], taco_id)

    def test_get_one_restaurant_bad_id(self):
        response = self.client.get(f'/api/v1/restaurants/123456/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        content = json.loads(response.content)

        self.assertEqual(content['detail'], 'Not found.')

    def test_restaurants_retrieve(self):
        response = self.client.get('/api/v1/restaurants/retrieve/', {'lat': 30, 'lng': -104})
        data ={
            "id": 2,
            "yelp_id": "DmpNJIjh1MtlnN36qw_9dw",
            "name": "Marfa Burrito",
            "phone": "",
            "is_closed": False,
            "review_count": 137,
            "yelp_rating": 4,
            "url": "https://www.yelp.com/biz/marfa-burrito-marfa-2?adjust_creative=pxQ3XEqH9sM15FQYWsuBXQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=pxQ3XEqH9sM15FQYWsuBXQ",
            "latitude": 30.3064881396931,
            "longitude": -104.019323420231,
            "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/-6-hdZM4A9i3SNArPp_bnw/o.jpg",
            "address": "S Highland Ave, Marfa, TX 79843",
            "tacoboutit_item_review_count": 0,
            "tacos": []
        }
        content = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(content[0]['yelp_id'], data['yelp_id'])
        self.assertEqual(content[0]['name'], data['name'])
        self.assertEqual(content[0]['phone'], data['phone'])
        self.assertEqual(content[0]['is_closed'], data['is_closed'])
        self.assertEqual(content[0]['review_count'], data['review_count'])
        self.assertEqual(content[0]['yelp_rating'], data['yelp_rating'])
        self.assertEqual(content[0]['url'], data['url'])
        self.assertEqual(content[0]['latitude'], data['latitude'])
        self.assertEqual(content[0]['longitude'], data['longitude'])
        self.assertEqual(content[0]['image_url'], data['image_url'])
        self.assertEqual(content[0]['address'], data['address'])
        self.assertEqual(content[0]['tacoboutit_item_review_count'], data['tacoboutit_item_review_count'])
        self.assertEqual(content[0]['tacos'], data['tacos'])

    def test_restaurants_retrieve_no_params(self):
        response = self.client.get('/api/v1/restaurants/retrieve/')
        content = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['error'], 'Please Provide a latitude and longitude')

    def test_restaurants_retrieve_no_restaurants(self):
        response = self.client.get('/api/v1/restaurants/retrieve/', {'lat': 1, 'lng': 4})
        content = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(content['status'], 'Resource Not Found')

class ReviewTestCase(APITestCase):
    def setUp(self):
        restuarant = Restaurant.objects.create(name='scotts tacos',
                        yelp_id = "akbkhadfb",
                        phone = "123456789",
                        is_closed = False,
                        review_count = 10,
                        yelp_rating = 4.7,
                        url = "http.hfhsf",
                        latitude = 47.60934,
                        longitude = -122.34076,
                        image_url = "https://s3-media3.fl.yelpcdn.com/bphoto/LFo_pxrIEmbVhkKSzZ0jiA/o.jpg",
                        address = "1521 1st Ave, Seattle, WA 98101",
                        distance = 100.7,
                        tacoboutit_item_review_count = 0)
        taco = Taco.objects.create(type='al pastor test taco', restaurant_id=restuarant.id)
        review = Review.objects.create(rating=7, review='terrible', taco_id=taco.id)

    def test_get_all_reviews(self):
        taco_id = Taco.objects.get(type='al pastor test taco').id
        review_id = Review.objects.get(review='terrible').id
        response = self.client.get('/api/v1/reviews/')

        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['id'], review_id)
        self.assertEqual(response.data[0]['rating'], 7)
        self.assertEqual(response.data[0]['taco'], taco_id)

    def test_get_one_review(self):
        taco_id = Taco.objects.get(type='al pastor test taco').id
        review_id = Review.objects.get(review='terrible').id
        response = self.client.get(f'/api/v1/reviews/{review_id}/')

        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], review_id)
        self.assertEqual(response.data['rating'], 7)
        self.assertEqual(response.data['taco'], taco_id)

    def test_get_one_review_bad_id(self):
        response = self.client.get('/api/v1/reviews/433334/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        content = json.loads(response.content)

        self.assertEqual(content['detail'], 'Not found.')

    def test_post_review(self):
        taco_id = Taco.objects.get(type='al pastor test taco').id
        response = self.client.post('/api/v1/reviews/', {"rating": 10, "review": "is ok", "taco": taco_id})

        content = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(content['rating'], 10)
        self.assertEqual(content['review'], 'is ok')
        self.assertEqual(content['taco'], taco_id)

    def test_post_review_no_taco_id(self):
        taco_id = Taco.objects.get(type='al pastor test taco').id
        response = self.client.post('/api/v1/reviews/', {"rating": 10, "review": "is ok"})

        content = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['taco'][0], 'This field is required.')


    def test_post_review_bad_id(self):
        response = self.client.post('/api/v1/reviews/', {"rating": 10, "review": "is ok", "taco": 12345})

        content = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['taco'][0], 'Invalid pk "12345" - object does not exist.')

class TacoTestCase(APITestCase):
    def setUp(self):
        restuarant = Restaurant.objects.create(name='scotts tacos',
                        yelp_id = "akbkhadfb",
                        phone = "123456789",
                        is_closed = False,
                        review_count = 10,
                        yelp_rating = 4.7,
                        url = "http.hfhsf",
                        latitude = 47.60934,
                        longitude = -122.34076,
                        image_url = "https://s3-media3.fl.yelpcdn.com/bphoto/LFo_pxrIEmbVhkKSzZ0jiA/o.jpg",
                        address = "1521 1st Ave, Seattle, WA 98101",
                        distance = 100.7,
                        tacoboutit_item_review_count = 0)
        taco = Taco.objects.create(type='al pastor test taco', restaurant_id=restuarant.id)
        review = Review.objects.create(rating=7, review='terrible', taco_id=taco.id)

    def test_get_all_tacos(self):
        taco_id = Taco.objects.get(type='al pastor test taco').id
        review_id = Review.objects.get(review='terrible').id
        response = self.client.get('/api/v1/tacos/')

        self.assertEqual(Taco.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['id'], taco_id)
        self.assertEqual(response.data[0]['type'], 'al pastor test taco')
        self.assertEqual(response.data[0]['average_rating'], 7.0)
        self.assertEqual(response.data[0]['reviews'][0]['id'], review_id)

    def test_get_one_taco(self):
        taco_id = Taco.objects.get(type='al pastor test taco').id
        review_id = Review.objects.get(review='terrible').id
        response = self.client.get(f'/api/v1/tacos/{taco_id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], taco_id)
        self.assertEqual(response.data['type'], 'al pastor test taco')
        self.assertEqual(response.data['average_rating'], 7.0)
        self.assertEqual(response.data['reviews'][0]['id'], review_id)

    def test_get_one_taco_bad_id(self):
        response = self.client.get('/api/v1/tacos/433334/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        content = json.loads(response.content)

        self.assertEqual(content['detail'], 'Not found.')

    # def test_post_taco(self):
    #     taco_id = Taco.objects.get(type='al pastor test taco').id
    #     restaurant_id = Restaurant.objects.get(name='scotts tacos').id
    #     response = self.client.post('/api/v1/tacos/new/',{'type':'cabeza', 'restaurant': restaurant_id})
    #     content = json.loads(response.content)
    #
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(content['rating'], 10)
    #     self.assertEqual(content['review'], 'is ok')
    #     self.assertEqual(content['taco'], taco_id)

class UserTestCase(APITestCase):
    def setUp(self):
        User.objects.create(username='taco', email='email@email.com')

    def test_get_all_users(self):
        response = self.client.get('/api/v1/users/')

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['username'], 'taco')
        self.assertEqual(response.data[0]['email'], 'email@email.com')

    def test_get_one_user(self):
        user_id = User.objects.get(username='taco').id
        response = self.client.get(f'/api/v1/users/{user_id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'taco')
        self.assertEqual(response.data['email'], 'email@email.com')

    def test_get_one_user_bad_id(self):
        response = self.client.get('/api/v1/users/433334/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        content = json.loads(response.content)

        self.assertEqual(content['detail'], 'Not found.')

    def test_post_one_user(self):
        response = self.client.post('/api/v1/users/', {'username':'taco', 'email':'email@email1.com'} )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        content = json.loads(response.content)

        self.assertEqual(response.data['username'], 'taco')
        self.assertEqual(response.data['email'], 'email@email1.com')

    def test_post_one_user(self):
        response = self.client.post('/api/v1/users/', {'username':'taco', 'email':'email@email.com'} )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        content = json.loads(response.content)


        self.assertEqual(response.data['email'][0], 'user with this email already exists.')
