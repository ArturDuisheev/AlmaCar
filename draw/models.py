from django.db import models
from django.contrib.postgres.fields import ArrayField
from account.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=100, unique=True)
    box_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'розыгрыш'
        verbose_name_plural = 'розыгрыши'

    def __str__(self):
        return self.title


class Prize(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='prizes')
    index = models.IntegerField(verbose_name="Номер коробки")
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'приз'
        verbose_name_plural = 'призы'
        unique_together = ('index', 'game')

    def __str__(self):
        return f"{self.title}-{str(self.game)}"


class OpenedBox(models.Model):
    index = models.IntegerField(verbose_name="Номер коробки")
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'открытый бокс'
        verbose_name_plural = 'открытые боксы'
        unique_together = ('index', 'game')

    def __str__(self):
        return f"{self.index}-{str(self.game)}"


class Winner(models.Model):
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE, verbose_name="приз")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")

    class Meta:
        verbose_name = 'победитель'
        verbose_name_plural = 'победители'

    def __str__(self):
        return f"{str(self.user.username)} выиграл (-а) {str(self.prize)}"


# class Rental(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     start_date = models.DateField()
#     end_date = models.DateField()
#
#     def __str__(self):
#         return f"{self.user} - {self.start_date} - {self.end_date}"

# class Meta:
#     verbose_name = "Последняя аренда"
#     verbose_name_plural = "последние аренды"

# @receiver(pre_save, sender=Box)
# def convert_prizes_to_array(sender, instance, **kwargs):
#     if isinstance(instance.prizes, list):
#         instance.prizes = instance.prizes
#     elif isinstance(instance.prizes, str):
#         instance.prizes = instance.prizes.split('\n')
