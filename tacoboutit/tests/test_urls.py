
import json
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from decouple import config
from django.utils.html import escape

#rest and taco show pages /:id
#tacos/new/
#tacos -- test to see if review data comes in response


class ApiTestCase(APITestCase):
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
            "distance": 34130.494208487944,
            "tacoboutit_item_review_count": 0,
            "tacos": []
        }
        content = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(content[0]['id'])
        self.assertEqual(content[0]['id'], data['id'])
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
        self.assertEqual(content[0]['distance'], data['distance'])
        self.assertEqual(content[0]['tacoboutit_item_review_count'], data['tacoboutit_item_review_count'])
        self.assertEqual(content[0]['tacos'], data['tacos'])

# class RestaurantModel:
#class ReviewModel:
#class taco model
