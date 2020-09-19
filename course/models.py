from django.db import models


class Discipline(models.Model):
    discipline_name = models.CharField(max_length=150, verbose_name='Название курса')
    discipline_description = models.CharField(max_length=250, verbose_name='Описание курса', null=True, blank=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.discipline_name


class Assignment(models.Model):
    discipline = models.ForeignKey(Discipline, related_name='discipline_assignment', verbose_name='Курс', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='Название')
    assignment_description = models.CharField(max_length=250, verbose_name='Описание', null=True, blank=True)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'




class AssignmentTaskFile(models.Model):
    assignment = models.ForeignKey(Assignment, related_name='assignment_file', on_delete=models.CASCADE)
    file = models.FileField(upload_to=f"files/assignments/%Y/%m%d", verbose_name='Файл')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'



class AssignmentItem(models.Model):
    assignment = models.ForeignKey(Assignment, related_name='assignment_item', on_delete=models.CASCADE)

