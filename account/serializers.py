from rest_framework import serializers
from .models import User, Comment, PromoCode


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class RegisterUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20)
    phone_number = serializers.CharField(max_length=20)
    inn = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20, write_only=True)
    password_2 = serializers.CharField(max_length=20, write_only=True)
    sms_code = serializers.CharField(max_length=20, write_only=True)
    promo_code = serializers.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = 'username phone_number inn password password_2 sms_code promo_code'.split()

    def validate(self, data):
        if data['password'] != data['password_2']:
            raise serializers.ValidationError('Пароли должны совпадать')
        fire_base = '123456'
        if data['sms_code'] != fire_base:
            raise serializers.ValidationError('Cмс код не совпадает')
        return data

    def create(self, validated_data):
        try:
            if PromoCode.objects.filter(code=validated_data['promo_code']).exists():
                user = User(
                    username=validated_data['username'],
                    phone_number=validated_data['phone_number'],
                    inn=validated_data['inn'],
                    promotion=True)
                user.set_password(validated_data['password'])
                user.save()
            else:
                user = User(
                    username=validated_data['username'],
                    phone_number=validated_data['phone_number'],
                    inn=validated_data['inn'])
                user.set_password(validated_data['password'])
                user.save()
                return user
        except Exception as e:
            raise serializers.ValidationError(f'Не удалось создать пользователя. {e}')



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'photo user description'.split()

    def get_name(self, obj):
        return str(obj.user.username)
