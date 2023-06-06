from django.db import models


class CardInCondition(models.Model):
    image = models.ImageField(upload_to='card_in_condition', verbose_name="Изображение")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Карточка c условием"
        verbose_name_plural = "Карточки с условием"
