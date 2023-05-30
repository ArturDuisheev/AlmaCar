from django.contrib import admin

from .models import Prize, Box, MoreInfo

admin.site.register(Prize)
admin.site.register(Box)
# admin.site.register(Rental)
admin.site.register(MoreInfo)
