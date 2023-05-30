from django.db import models
from django.contrib.postgres.fields import ArrayField
from account.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

from django.db import models
from multiselectfield import MultiSelectField

from django.db import models
from multiselectfield import MultiSelectField


class Box(models.Model):
    rows = models.PositiveIntegerField(verbose_name="сколько рядов")
    columns = models.PositiveIntegerField(verbose_name="сколько столбцов")
    prizes = models.TextField(verbose_name="призы", max_length=100)

    def __str__(self):
        return f"{self.rows}x{self.columns}"

    class Meta:
        verbose_name = "ячейка"
        verbose_name_plural = "ячейки"


class Prize(models.Model):
    row = models.PositiveIntegerField(verbose_name="ряд")
    column = models.PositiveIntegerField(verbose_name="столбец")
    prize_item = models.CharField(max_length=100, verbose_name="приз")
    box = models.ManyToManyField(Box, verbose_name="ячейка")

    def __str__(self):
        return f"{self.row}x{self.column}"

    class Meta:
        verbose_name = "Приз"
        verbose_name_plural = "Призы"


class MoreInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name="название розыгрыша")
    how_prize_true = models.TextField(max_length=100, verbose_name="В данном розыгрыше присутствуют такие призы как: ")
    winners = models.ForeignKey(User, verbose_name="Победители", on_delete=models.CASCADE, null=True)
    how_prize_win = models.ForeignKey(Prize, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подробнее про розыгрыш"
        verbose_name_plural = "Подробнее про розыгрыши"


# class Rental(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     start_date = models.DateField()
#     end_date = models.DateField()
#
#     def __str__(self):
#         return f"{self.user} - {self.start_date} - {self.end_date}"

    class Meta:
        verbose_name = "Последняя аренда"
        verbose_name_plural = "последние аренды"

# @receiver(pre_save, sender=Box)
# def convert_prizes_to_array(sender, instance, **kwargs):
#     if isinstance(instance.prizes, list):
#         instance.prizes = instance.prizes
#     elif isinstance(instance.prizes, str):
#         instance.prizes = instance.prizes.split('\n')
