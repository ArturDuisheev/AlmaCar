from rest_framework import serializers

from .models import ItemAddition


class ItemAdditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemAddition
        fields = 'id image name price hour'.split()

