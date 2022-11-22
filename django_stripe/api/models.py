from django.db import models


class Item(models.Model):
    name = models.CharField(
        'Наименование',
        max_length=200
    )
    description = models.TextField('Описание товара')
    price = models.DecimalField('Цена',
                                decimal_places=2,
                                max_digits=10)
    image = models.ImageField(
        'Изображение товара',
        upload_to='items/',
        blank=True,
        help_text='Изображение товара'
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
