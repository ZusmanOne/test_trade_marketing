from django.db import models
from django.core.validators import MinValueValidator


class Statistic(models.Model):
    event_date = models.DateTimeField(db_index=True, verbose_name='Дата события')
    views = models.IntegerField(verbose_name='Количество показов', blank=True)
    clicks = models.IntegerField(verbose_name='Количество кликов', blank=True)
    cost = models.DecimalField(
        verbose_name='Стоимость',
        max_digits=8, decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return f'{self.pk} - {self.event_date}'


# Create your models here.
