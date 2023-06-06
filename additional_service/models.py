from django.db import models


class ItemAddition(models.Model):
    image = models.ImageField(upload_to='images/', verbose_name="изображение доп услуги")
    name = models.CharField(max_length=150, verbose_name="Наименование доп услуги")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена доп услуги")
    hour = models.CharField(max_length=100, verbose_name="Время доп услуги", blank=True, null=True)

    def __str__(self):
        return f"{self.name} {str(self.price)}"

    class Meta:
        verbose_name = "Дополнительная услуга"
        verbose_name_plural = "Дополнительные услуги"



