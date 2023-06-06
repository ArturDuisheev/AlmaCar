from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from main_page.models import DetailCar, RentCar
from .managers import CustomUserManager
import shortuuid


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, verbose_name='ФИО', null=True)
    phone_number = models.CharField(max_length=50, unique=True, verbose_name='Номер телефона')
    inn = models.CharField(max_length=50, verbose_name='ИНН')
    promotion = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False, verbose_name="Менеджер")
    is_superuser = models.BooleanField(default=False, verbose_name="Суперпользователь")
    attempts = models.IntegerField(default=0, verbose_name="Количество попыток в розыгрыше")
    bonus = models.ForeignKey(DetailCar, to_field='bonus', on_delete=models.CASCADE, null=True, blank=True, related_name="boneses")
    history = models.ForeignKey(RentCar, verbose_name='История аренды', related_name='user_history', blank=True, null=True, on_delete=models.CASCADE)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(fields=['username'], name='unique_username'),
        ]

    def __str__(self):
        return self.phone_number

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        uuid = shortuuid.uuid()
        promo_code = uuid[:8]
        code = PromoCode.objects.filter(code=promo_code).exists()
        while code:
            promo_code = uuid[:8]
            code = PromoCode.objects.filter(code=promo_code).exists()
        user = User.objects.get(pk=self.id)
        PromoCode.objects.create(code=promo_code, user=user)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    description = models.TextField(verbose_name='Отзыв')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Список промокодов'

    def __str__(self):
        return self.code


class MyProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="users_profile")
    car = models.ForeignKey(DetailCar, on_delete=models.CASCADE, verbose_name="Арендованная машина", related_name="user_car_rent")

    def __str__(self) -> str:
        return str(self.user)

    class Meta:
        db_table = "profile"
        verbose_name = "Профиль"
        verbose_name_plural = "Профиль"


class Bonus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_bonus")
    bonus = models.ForeignKey(DetailCar, on_delete=models.CASCADE, related_name="bonuses")

    def __str__(self) -> str:
        return str(self.user)

    class Meta:
        db_table = "bonus_user"
        verbose_name = "Бонус"
        verbose_name_plural = "Бонусы"
