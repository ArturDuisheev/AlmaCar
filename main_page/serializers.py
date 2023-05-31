from rest_framework import serializers

from .models import OurCar, DetailCar, Award


class OurCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurCar
        fields = '__all__'


class DetailCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetailCar
        fields = '__all__'



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
