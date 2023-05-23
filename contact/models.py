from django.db import models


class Contact(models.Model):
    phone_number_first = models.CharField(max_length=45, verbose_name="Первый номер телефона")
    phone_number_second = models.CharField(max_length=45, blank=True, null=True, verbose_name="Второй номер телефона")
    email = models.EmailField(verbose_name="Почта")
    hour_working = models.CharField(max_length=200, verbose_name="Время работы")
    city = models.CharField(max_length=250, verbose_name="Город")

    def __str__(self):
        return self.phone_number_first

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"
