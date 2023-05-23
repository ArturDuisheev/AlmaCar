from django.db import models

from account.models import User


class OurCar(models.Model):
    name_car = models.CharField(max_length=100, verbose_name="Модель машины")
    image_car = models.ImageField(upload_to='cars_main_page/', verbose_name="Изображение машины")
    price = models.CharField(max_length=150, verbose_name="Цена машины")
    year_car = models.IntegerField(verbose_name="Год машины")

    def __str__(self):
        return self.name_car

    class Meta:
        verbose_name = "Наша машина"
        verbose_name_plural = "Наши машины"


class DetailCar(models.Model):
    image_car = models.ImageField(upload_to='cars_detail_page/', verbose_name="Изображение машины")
    image_brand = models.ImageField(upload_to='cars_brand_page/', verbose_name="Изображение марки машины")
    name_car = models.CharField(max_length=100, verbose_name="Модель машины")
    color = models.CharField(max_length=100, verbose_name="Цвет машины")
    year_car = models.IntegerField(verbose_name="Год выпуска машины")
    engine_capacity = models.CharField(max_length=100, verbose_name="Обьем двигателя машины")
    transmission = models.CharField(max_length=100, verbose_name="Коробка передач машины")
    equipment = models.CharField(max_length=100, verbose_name="Комплектация")
    price = models.CharField(max_length=100, verbose_name="Цена машины")
    pledge = models.CharField(max_length=100, verbose_name="Залог")
    image_car_first = models.ImageField(upload_to='cars_detail/', verbose_name="Изображение 1")
    image_car_second = models.ImageField(upload_to='cars_detail/', verbose_name="Изображение 2", blank=True, null=True)
    image_car_third = models.ImageField(upload_to='cars_detail/', verbose_name="Изображение 3", blank=True, null=True)
    image_car_fourth = models.ImageField(upload_to='cars_detail/', verbose_name="Изображение 4", blank=True, null=True)
    image_car_fifth = models.ImageField(upload_to='cars_detail/', verbose_name="Изображение 5", blank=True, null=True)
    image_car_sixth = models.ImageField(upload_to='cars_detail/', verbose_name="Изображение 6", blank=True, null=True)
    image_car_seventh = models.ImageField(upload_to='cars_detail/', verbose_name="Изображение 7", blank=True, null=True)

    def __str__(self):
        return self.name_car

    class Meta:
        verbose_name = "Детальная информация о машине"
        verbose_name_plural = "Детальная информация о машине"


# class Comment(models.Model):
#     photo = models.ImageField(upload_to='photos_in_comment/', verbose_name="Фото профиля")
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
#     description = models.TextField(verbose_name="Отзыв")
#
#     def __str__(self):
#         return self.user.username
#
#     class Meta:
#         verbose_name = "Отзыв"
#         verbose_name_plural = "Отзывы"


class Award(models.Model):
    name_award = models.CharField(max_length=100, verbose_name="Наименование награды")
    award_image = models.ImageField(upload_to='awards_image/', verbose_name="Фото награды")

    def __str__(self):
        return self.name_award

    class Meta:
        verbose_name = "Награда"
        verbose_name_plural = "Награды"
