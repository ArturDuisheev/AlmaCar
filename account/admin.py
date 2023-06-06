from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(PromoCode)
admin.site.register(Comment)
admin.site.register(MyProfile)
admin.site.register(Bonus)


