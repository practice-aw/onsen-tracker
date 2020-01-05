from django.urls import include, path
from rest_framework import routers
from . import views
# figure out out to remove trailing slash requirement
router = routers.DefaultRouter()
router.register(r'tacos', views.TacoViewSet)
router.register(r'restaurants', views.RestaurantViewSet)
router.register(r'reviews', views.ReviewViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/v1/restaurants/retrieve/', views.RestaurantUpdateOrCreateViewSet.retrieve, name='update_or_create'),
    path('api/v1/tacos/new/', views.TacoViewSet.post_new, name='new_taco'),
    path(r'api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
