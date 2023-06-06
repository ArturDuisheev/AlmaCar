from rest_framework import serializers

from draw.models import Game, OpenedBox, Prize, Winner
from django.contrib.auth import get_user_model

User = get_user_model()


class PrizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prize
        fields = 'id title image index'.split()


class GameSerializer(serializers.ModelSerializer):
    prizes = PrizeSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = 'id title box_count prizes'.split()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['winners'] = [str(winner) for winner in Winner.objects.filter(prize__game=instance)]
        data['opened_boxes'] = [box.get('index') for box in OpenedBox.objects.filter(game=instance).values('index')]
        return data


class OpenedBoxCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenedBox
        fields = 'game index'.split()

    def validate(self, attrs):
        if isinstance(attrs['game'], int):
            game = Game.objects.get(id=attrs['game'])
        else:
            game = attrs['game']
        if game.box_count < attrs['index']:
            raise serializers.ValidationError('Box index is out of range')
        if self.context['request'].user.attempts == 0:
            raise serializers.ValidationError('You have no attempts left')
        user = self.context['request'].user
        user.attempts -= 1
        user.save()
        if OpenedBox.objects.filter(game=game, index=attrs['index']).exists():
            raise serializers.ValidationError('Box is already opened')
        return attrs
