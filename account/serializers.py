from rest_framework import serializers
from .models import User, Comment


class RegisterAuthorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=16)

    class Meta:
        model = User
        fields = 'username email password'.split()

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = 'photo user description'.split()

    def get_name(self, obj):
        return str(obj.user.username)

