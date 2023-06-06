from rest_framework import serializers
from .models import User, Comment, PromoCode, MyProfile, Bonus

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from contact.serializers import AccountEmailSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class RegisterUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20)
    phone_number = serializers.CharField(max_length=20)
    inn = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20, write_only=True)
    password_2 = serializers.CharField(max_length=20, write_only=True)
    promo_code = serializers.CharField(max_length=20, required=False, allow_null=True)

    class Meta:
        model = User
        fields = 'username phone_number inn password password_2 promo_code'.split()

    def validate(self, data):
        if data['password'] != data['password_2']:
            raise serializers.ValidationError('Пароли должны совпадать')
        # fire_base = '123456'
        # if data['sms_code'] != fire_base:
        #     raise serializers.ValidationError('Cмс код не совпадает')
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
                return user
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
        fields = 'id user description'.split()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = instance.user.username
        return data

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False

    def validate(self, attrs):
        attrs.update({'password': ''})
        return super(MyTokenObtainPairSerializer, self).validate(attrs)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['phone_number'] = user.phone_number
        return token


class ContactSerializer(serializers.ModelSerializer):
    contacts = AccountEmailSerializer(many=True)

    class Meta:
        model = User
        fields = (
            "username",
            "phone_number",
            "inn",
            "contacts",
        )


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    car = serializers.StringRelatedField()

    class Meta:
        model = MyProfile
        fields = (
            "user",
            "car",
        )
        read_only_fields = fields


class BonusUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = (
            "user",
            "bonus",
        )

