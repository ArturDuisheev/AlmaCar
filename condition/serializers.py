from rest_framework import serializers

from .models import CardInCondition


class CardInConditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CardInCondition
        fields = 'id image title description'.split()
