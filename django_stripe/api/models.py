from django.db import models

class Item(models.Model):
    name = models.CharField(
        'Наименование',
        max_length=200
    )
    description = models.TextField('Описание товара')
    price = models.IntegerField('Цена')
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
