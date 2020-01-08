
# Tacoboutit Backend

In this group project, we build a Restful Python DJANGO API that exposes endpoints for a React-Native
front end application. The backend application consumes Yelp API business data based off of
given coordinates from the user. That data is then filtered using alorithms in the backend and saved into 
our database with a newly generated ID. This restaurant data enables users to create post tacos for a specific restaurant, create reviews for specific tacos, as well as pulling and reviewing this data. 

## Schema Design

![tacoboutiterd](https://user-images.githubusercontent.com/33855435/72005861-c2a76200-320b-11ea-8f7c-80125e5b7944.jpg)


## Data Flow Example: 
### Endpoint api/v1/restaurants/retrieve?lat=40&lng=-140 
![tacoboutit](https://user-images.githubusercontent.com/33855435/72001432-b539aa00-3202-11ea-9685-707345feb14d.jpg)

## Getting Started
Heroku: https://tacoboutit-backend.herokuapp.com

Postman[https://www.getpostman.com/downloads/] can be used to make HTTP requests.

Front-end Repository: https://github.com/TakoBoutIt/tacoboutit-frontend


# Endpoints
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
{
    "id": 37,
    "type": "carne asada",
    "restaurant_id": 46,
    "average_rating": 10.0,
    "reviews": [
        {
            "id": 52,
            "rating": 10.0,
            "review": "is ok",
            "taco": 37
        }
    ]
}
```
### GET /api/v1/restaurants/1 (:id)
Response:
```
{
    "id": 46,
    "yelp_id": "IhQvn84o-VuCMg6oDJ-tiQ",
    "name": "Acapulco Bay",
    "phone": "+19705426400",
    "is_closed": false,
    "review_count": 34,
    "yelp_rating": 3.0,
    "url": "https://www.yelp.com/biz/acapulco-bay-fort-morgan?adjust_creative=pxQ3XEqH9sM15FQYWsuBXQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=pxQ3XEqH9sM15FQYWsuBXQ",
    "latitude": 40.2486933123126,
    "longitude": -103.801294020832,
    "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/zSJ73wV6dFvhxRWeYMU7hw/o.jpg",
    "address": "200 Main St, Fort Morgan, CO 80701",
    "distance": 32405.9929463048,
    "tacoboutit_item_review_count": 0,
    "tacos": [
        {
            "id": 37,
            "type": "carne asada",
            "restaurant_id": 46,
            "average_rating": 10.0,
            "reviews": [
                {
                    "id": 52,
                    "rating": 10.0,
                    "review": "is ok",
                    "taco": 37
                }
            ]
        }
    ]
}
```
### GET /api/v1/restaurants/retrieve
Params: 
```
Params: /api/v1/restaurants/retrieve/?lat=39.7392&lng=-104.9903
```
Response:
```
[
    {
        "id": 46,
        "yelp_id": "IhQvn84o-VuCMg6oDJ-tiQ",
        "name": "Acapulco Bay",
        "phone": "+19705426400",
        "is_closed": false,
        "review_count": 34,
        "yelp_rating": 3.0,
        "url": "https://www.yelp.com/biz/acapulco-bay-fort-morgan?adjust_creative=pxQ3XEqH9sM15FQYWsuBXQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=pxQ3XEqH9sM15FQYWsuBXQ",
        "latitude": 40.2486933123126,
        "longitude": -103.801294020832,
        "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/zSJ73wV6dFvhxRWeYMU7hw/o.jpg",
        "address": "200 Main St, Fort Morgan, CO 80701",
        "distance": 32405.9929463048,
        "tacoboutit_item_review_count": 0,
        "tacos": []
    },
    {
        "id": 47,
        "yelp_id": "crdZRXwGcOxegraxkHVk5g",
        "name": "Corona's Mexican Grill-Strasburg",
        "phone": "+13036224959",
        "is_closed": false,
        "review_count": 63,
        "yelp_rating": 3.5,
        "url": "https://www.yelp.com/biz/coronas-mexican-grill-strasburg-strasburg?adjust_creative=pxQ3XEqH9sM15FQYWsuBXQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=pxQ3XEqH9sM15FQYWsuBXQ",
        "latitude": 39.7390207,
        "longitude": -104.3296081,
        "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/0euFFmohCDArPe1ecQ4Gwg/o.jpg",
        "address": "56171 E Colfax Ave, Strasburg, CO 80136",
        "distance": 40415.4182050924,
        "tacoboutit_item_review_count": 0,
        "tacos": []
    },
    {
        "id": 48,
        "yelp_id": "bpoxdIjDE9tMmojiS6limQ",
        "name": "EL Jacal Mexican Grill",
        "phone": "+19708671115",
        "is_closed": false,
        "review_count": 47,
        "yelp_rating": 3.0,
        "url": "https://www.yelp.com/biz/el-jacal-mexican-grill-fort-morgan?adjust_creative=pxQ3XEqH9sM15FQYWsuBXQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=pxQ3XEqH9sM15FQYWsuBXQ",
        "latitude": 40.25836,
        "longitude": -103.80184,
        "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/GCMb3BMwc1if4e2X8FZ_OA/o.jpg",
        "address": "903 Main St, Fort Morgan, CO 80701",
        "distance": 33305.995870968,
        "tacoboutit_item_review_count": 0,
        "tacos": []
    },
    {
        "id": 49,
        "yelp_id": "KgGGiv6tpRgaL-kq1G_uLQ",
        "name": "Rookies Saloon and Restaurant",
        "phone": "+13036229750",
        "is_closed": false,
        "review_count": 14,
        "yelp_rating": 4.0,
        "url": "https://www.yelp.com/biz/rookies-saloon-and-restaurant-strasburg?adjust_creative=pxQ3XEqH9sM15FQYWsuBXQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=pxQ3XEqH9sM15FQYWsuBXQ",
        "latitude": 39.735577,
        "longitude": -104.321918,
        "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/2lcE2INCYZVZYPeqFJWvng/o.jpg",
        "address": "1323 Monroe St, Strasburg, CO 80136",
        "distance": 40240.8151816399,
        "tacoboutit_item_review_count": 0,
        "tacos": []
    },
    {
        "id": 50,
        "yelp_id": "neXr7HI4v1dtEqKcazK7HQ",
        "name": "Santiago's Mexican Restaurant",
        "phone": "+19708672214",
        "is_closed": false,
        "review_count": 16,
        "yelp_rating": 3.5,
        "url": "https://www.yelp.com/biz/santiagos-mexican-restaurant-fort-morgan?adjust_creative=pxQ3XEqH9sM15FQYWsuBXQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=pxQ3XEqH9sM15FQYWsuBXQ",
        "latitude": 40.25438,
        "longitude": -103.81319,
        "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/E9e4TzQ28t9qouAunIejHQ/o.jpg",
        "address": "901 W Platte Ave, Fort Morgan, CO 80701",
        "distance": 32429.6568269428,
        "tacoboutit_item_review_count": 0,
        "tacos": []
    }
]
```

### POST /api/v1/reviews
When I make the POST request with this information in the body:
```
{
    "rating": 10, 
    "review": "is ok", 
    "taco": 27
}

```
Response:
```
{
    "id": 8,
    "rating": 10.0,
    "review": "is ok",
    "taco": 27
}
```

### POST /api/v1/tacos/new/
The post request should be formatted as follows:
```
Body:
    { 
      "type": "carne asada", 
       "restaurant": 46
     }
```
Response:
```
Body:
    {  
     "success": "carne asada added to Taquería El Trompito"
    }
```
When the restaurant does not exist:
Response:
```
{ 
      "error": "A restaurant with id: 2382 does not exist"
}
```
When the taco already exists:
Response:
```
    "error": "carne asada already exists"
```

### For Developers:
## Setup instructions
1. Clone this repo
Install python: https://realpython.com/installing-python/
In terminal:
```
pip install django
```
```
pip install djangorestframework
```
```
pip install psycopg2
```
```
pip install requests
```
```
pip install requests
```

2. Create a virtual environment(venv) on your local environment

### Testing
install testing packs: 
```
pip install pytest
```
```
pip install pytest-django
```
```
pip install pytest-cov
```
```
pip install mixer
```
to run tests: 
```
py.test
```

### Core Contributors
Alec Wells Github: alect47

Scott Payton Github: scottzero
