from django.contrib import admin

from .models import OurCar, DetailCar, Award

admin.site.register(OurCar)
admin.site.register(DetailCar)
admin.site.register(Award)
