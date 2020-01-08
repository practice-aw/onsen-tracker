# Tacoboutit Backend

In this group project, we build a Restful Python DJANGO API that exposes endpoints for a React-Native
front end application. The backend application consumes Yelp API business data based off of
given coordinates from the user. That data is then filtered in backend alorithms and saved into 
our database with a newly generated ID. Using our internal API you can make a variety of HTTP requests related to 
specific Taco dishes. 

## Endpoints
### GET /api/v1/reviews
Response:
```
Body:
[
    {
        "id": 2,
        "rating": 4.0,
        "review": "test review",
        "taco": 27
    },
    {
        "id": 3,
        "rating": 4.0,
        "review": "test review",
        "taco": 27
    },
    {
        "id": 4,
        "rating": 4.0,
        "review": null,
        "taco": 27
    }
]
```
### GET /api/v1/tacos
Response:
```
body:
[
    {
        "id": 27,
        "type": "carne asada",
        "restaurant_id": 2361,
        "average_rating": 5.833333333333333,
        "reviews": [
            {
                "id": 2,
                "rating": 4.0,
                "review": "test review",
                "taco": 27
            },
            {
                "id": 3,
                "rating": 4.0,
                "review": "test review",
                "taco": 27
            }
          ]
       }
]
```
### GET /api/v1/tacos/1 (:id)
Response: 
```
Body:
{
    "id": 1,
    "type": "al pastor",
    "restaurant": 2361
}
```
### GET /api/v1/restaurants/1 (:id)
Response:
```
Body:
{
    "id": 2361,
    "yelp_id": "aRur9R9tTXqRgqb_NZQyBA",
    "name": "Casco Antiguo",
    "phone": "+12065380400",
    "is_closed": false,
    "review_count": 522,
    "yelp_rating": 4.0,
    "url": "https://www.yelp.com/biz/casco-antiguo-seattle-4?adjust_creative=pxQ3XEqH9sM15FQYWsuBXQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=pxQ3XEqH9sM15FQYWsuBXQ",
    "latitude": 47.601203,
    "longitude": -122.333255,
    "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/5z4fmEVq6oqvOZ0JWTd-zg/o.jpg",
    "address": "115 Occidental Ave S, Seattle, WA 98104",
    "distance": 770.6851931638339,
    "tacoboutit_item_review_count": 0,
    "tacos": [
        {
            "id": 27,
            "type": "carne asada",
            "restaurant_id": 2361,
            "average_rating": 5.833333333333333,
            "reviews": [
                {
                    "id": 2,
                    "rating": 4.0,
                    "review": "test review",
                    "taco": 27
                },
                {
                    "id": 3,
                    "rating": 4.0,
                    "review": "test review",
                    "taco": 27
                },
                {
                    "id": 4,
                    "rating": 4.0,
                    "review": null,
                    "taco": 27
                },
                {
                    "id": 5,
                    "rating": 4.0,
                    "review": null,
                    "taco": 27
                },
                {
                    "id": 6,
                    "rating": 10.0,
                    "review": null,
                    "taco": 27
                },
                {
                    "id": 7,
                    "rating": 9.0,
                    "review": null,
                    "taco": 27
                }
            ]
        },
        {
            "id": 28,
            "type": "al pastor",
            "restaurant_id": 2361,
            "average_rating": null,
            "reviews": []
        }
    ]
}
```
### GET /api/v1/restaurants
Params: 
```
Params: /api/v1/restaurants/retrieve/?lat=39.7392&lng=-104.9903
```
Response:
```
Body: 
[
    {
        "id": 2361,
        "yelp_id": "aRur9R9tTXqRgqb_NZQyBA",
        "name": "Casco Antiguo",
        "phone": "+12065380400",
        "is_closed": false,
        "review_count": 522,
        "yelp_rating": 4.0,
        "url": "https://www.yelp.com/biz/casco-antiguo-seattle-4?adjust_creative=pxQ3XEqH9sM15FQYWsuBXQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=pxQ3XEqH9sM15FQYWsuBXQ",
        "latitude": 47.601203,
        "longitude": -122.333255,
        "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/5z4fmEVq6oqvOZ0JWTd-zg/o.jpg",
        "address": "115 Occidental Ave S, Seattle, WA 98104",
        "distance": 770.6851931638339,
        "tacoboutit_item_review_count": 0,
        "tacos": [
            {
                "id": 27,
                "type": "carne asada",
                "restaurant": 2361
            },
            {
                "id": 28,
                "type": "al pastor",
                "restaurant": 2361
            }
        ]
    },
    {
        "id": 2362,
        "yelp_id": "dyN-UDqTKMk9lnv99DBbhw",
        "name": "La Cocina Oaxaquena",
        "phone": "+12066238226",
        "is_closed": false,
        "review_count": 464,
        "yelp_rating": 4.0,
        "url": "https://www.yelp.com/biz/la-cocina-oaxaquena-seattle?adjust_creative=pxQ3XEqH9sM15FQYWsuBXQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=pxQ3XEqH9sM15FQYWsuBXQ",
        "latitude": 47.6154747009277,
        "longitude": -122.328178405762,
        "image_url": "https://s3-media4.fl.yelpcdn.com/bphoto/X1Nc8XnQ6aqi3SXseOLQ8Q/o.jpg",
        "address": "1216 Pine St, Seattle, WA 98101",
        "distance": 974.2464664280571,
        "tacoboutit_item_review_count": 0,
        "tacos": []
    }
]
```



##Schema Design

<img width="1183" alt="Screen Shot 2020-01-07 at 11 02 11 PM" src="https://user-images.githubusercontent.com/33855435/71954283-0796ae80-31a2-11ea-974c-902dc9de5da6.png">

##Getting Started
Heroku: https://tacoboutit-test.herokuapp.com
Postman[https://www.getpostman.com/downloads/] can be used to make HTTP requests. 

