from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Coupon(models.Model):
    code = models.CharField(
        'Код купона',
        max_length=50,
        unique=True)
    valid_from = models.DateTimeField(
        'Действителен с',
    )
    valid_to = models.DateTimeField(
        'Действителен по',
    )
    discount = models.IntegerField(
        'Размер скидки в %',
        validators=[MinValueValidator(0),
                    MaxValueValidator(100)])
    active = models.BooleanField(
        'Активность купона'
    )

    def __str__(self):
        return self.code
