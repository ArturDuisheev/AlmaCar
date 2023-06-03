from django.contrib import admin

from .models import Game, OpenedBox, Winner, Prize

admin.site.register(Game)
admin.site.register(OpenedBox)
admin.site.register(Winner)
admin.site.register(Prize)

