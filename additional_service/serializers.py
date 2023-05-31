from rest_framework import serializers

from .models import ItemAddition


class ItemAdditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemAddition
        fields = 'id image name price hour'.split()

    def get_price_and_hour(self, obj):
        return f"{obj.price} / {obj.hour}"
