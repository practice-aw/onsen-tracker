
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
            "id": 1,
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
            "distance": 34130.4942084879,
            "tacoboutit_item_review_count": 0,
            "tacos": []
        }
        content = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(content[0],data)

    def test

# class RestaurantModel:
#class ReviewModel:
#class taco model
