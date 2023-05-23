from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=18)
    email = models.EmailField()


class Comment(models.Model):
    photo = models.ImageField(upload_to='photos_in_comment/', verbose_name="Фото профиля")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    description = models.TextField(verbose_name="Отзыв")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


