from django.contrib import admin
from .models import Hero
from .models import Restaurant, Taco

# Register your models here.
admin.site.register(Hero)
admin.site.register(Restaurant)
admin.site.register(Taco)
