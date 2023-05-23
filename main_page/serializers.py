from rest_framework import serializers

from .models import OurCar, DetailCar, Award


class OurCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurCar
        fields = '__all__'


class DetailCarSerializer(serializers.ModelSerializer):
    photos = serializers.ListField(child=serializers.FileField(), max_length=7, allow_empty=True, required=False)

    class Meta:
        model = DetailCar
        fields = '__all__'

    def create(self, validated_data):
        photos_data = validated_data.pop('photos', [])
        detail_car = DetailCar.objects.create(**validated_data)
        for photo_data in photos_data:
            DetailCar.objects.create(detail_car=detail_car, photo=photo_data)
        return detail_car

    def update(self, instance, validated_data):
        photos_data = validated_data.pop('photos', [])
        instance = super().update(instance, validated_data)
        DetailCar.objects.filter(detail_car=instance).delete()
        for photo_data in photos_data:
            DetailCar.objects.create(detail_car=instance, photo=photo_data)
        return instance


# class CommentSerializer(serializers.ModelSerializer):
#     # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     user = RegisterAuthorSerializer(
#         source="username", read_only=True
#     )
#
#     class Meta:
#         model = Comment
#         fields = 'photo user description'.split()
#
#     def get_name(self, obj):
#         return str(obj.user.username)


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = '__all__'
