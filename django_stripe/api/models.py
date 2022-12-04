from django.db import models


class Item(models.Model):
    name = models.CharField(
        'Наименование',
        max_length=200
    )
    description = models.TextField('Описание товара')
    price = models.IntegerField('Цена',
                                help_text='Цена товара в копейках')
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


class Сurrency(models.Model):
    name = models.CharField(
        'Наименование валюты',
        max_length=100
    )
    alphabetic_code = models.CharField(
        'Код валюты',
        max_length=5
    )
    currency_symbol = models.CharField(
        'Символ валюты',
        max_length=3
    )
    exchange_rate = models.DecimalField(
        'Курс обмена',
        max_digits=10,
        decimal_places=2,
        blank=False
    )
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

    def __str__(self):
        return self.name
