from django.db import models


class Discipline(models.Model):
    discipline_name = models.CharField(max_length=150, verbose_name='Название курса')
    discipline_description = models.CharField(max_length=250, verbose_name='Описание курса', null=True, blank=True)
    is_active = models.BooleanField('Активно?', default=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.discipline_name


