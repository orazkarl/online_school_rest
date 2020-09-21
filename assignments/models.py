from django.db import models

from courses.models import Discipline
from user_auth.admin import Student


class Assignment(models.Model):
    discipline = models.ForeignKey(Discipline, related_name='discipline_assignment', verbose_name='Курс',
                                   on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='Название')
    assignment_description = models.CharField(max_length=250, verbose_name='Описание', null=True, blank=True)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'


class AssignmentTaskFile(models.Model):
    assignment = models.ForeignKey(Assignment, related_name='assignment_file', on_delete=models.CASCADE)
    file = models.FileField(upload_to=f"files/assignments/tasks/%Y/%m%d", verbose_name='Файл')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class AssignmentAnswer(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='assignment_item_student',
                                   verbose_name='Студент')
    assignment = models.ForeignKey(Assignment, related_name='answer', on_delete=models.CASCADE, verbose_name='Задания')

    answer_file = models.FileField(upload_to=f"files/assignments/answers/%Y/%m%d", verbose_name='Файл')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
