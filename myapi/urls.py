from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tacos', views.TacoViewSet)
router.register(r'restaurants', views.RestaurantViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('api/v1/restaurants/retrieve/', views.RestaurantUpdateOrCreateViewSet.retrieve, name='update_or_create'),
    path('api/v1/tacos/new/', views.TacoViewSet.post_new, name='new_taco'),
    path(r'api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
