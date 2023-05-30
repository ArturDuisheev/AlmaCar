from rest_framework import serializers

from .models import Box, Prize, MoreInfo


class PrizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prize
        fields = ('id', 'row', 'column', 'prize_item', 'box')


class BoxSerializer(serializers.ModelSerializer):
    prizes = serializers.CharField()

    class Meta:
        model = Box
        fields = ('id', 'rows', 'columns', 'prizes')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        prizes = data.get('prizes', '')
        if isinstance(prizes, str):
            values = [value.strip() for value in prizes.split(',') if value.strip()]
            data['prizes'] = values
        return data


class MoreInfoSerializer(serializers.ModelSerializer):
    how_prize_true = serializers.SerializerMethodField()

    class Meta:
        model = MoreInfo
        fields = ('id', 'name', 'how_prize_true', 'winners', 'how_prize_win')

    def get_winners(self, instance):
        winner_name = instance.winners.name if instance.winners else ""
        prize = instance.how_prize_win.prize_item if instance.how_prize_win else ""
        return f"{winner_name} выиграл(-а) {prize}"

    def get_how_prize_true(self, obj):
        return obj.how_prize_true


# class RentalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Rental
#         fields = '__all__' n
