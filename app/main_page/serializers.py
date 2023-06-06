from rest_framework import serializers

from account.models import User
from main_page.models import (
    DetailCar,
    Award,
    CarImage,
    AboutCompany

)


class CarImageInnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = '__all__'


class DetailCarSerializer(serializers.ModelSerializer):
    images = CarImageInnerSerializer(many=True)
    bonus = serializers.SerializerMethodField(method_name='get_bonus')

    class Meta:
        model = DetailCar
        fields = (
            'id', 'image_car', 'image_brand', 'name_car', 'name_car_brand', 'color', 'year_car', 'engine_capacity',
            'transmission',
            'equipment', 'price', 'pledge', 'images', 'hour', 'bonus', 'status'
        )

    def get_bonus(self, obj):
        if obj.status == "Завершен":
            return obj.bonus + 800
        else:
            return 0
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


class AboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompany
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        video = data.get('video', '')
        if isinstance(video, str):
            values = [value.strip() for value in video.split(',') if value.strip()]
            data['video'] = values
        return data


class ActiveDetailCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailCar
        fields = ('name_car', 'name_car_brand', 'start', 'end',  'price',  'status', 'hour')