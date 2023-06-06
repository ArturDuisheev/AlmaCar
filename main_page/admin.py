from django.contrib import admin

from .models import DetailCar, Award, CarImage, RentCar

admin.site.register(DetailCar)
admin.site.register(Award)
admin.site.register(CarImage)


@admin.register(RentCar)
class RentCarAdmin(admin.ModelAdmin):
    list_display = ["rent_car", "user", "remaining_time"]



