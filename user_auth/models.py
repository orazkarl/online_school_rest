from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from courses.models import Discipline

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class StudentGroup(models.Model):
    name = models.CharField(max_length=100, verbose_name='Названия груупы')
    disciplines = models.ManyToManyField(Discipline, blank=True, related_name='student_groups')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class User(AbstractUser):
    email = models.EmailField(_('Email address'), unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='Номер телефона')
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name='Адрес')
    dob = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    is_student = models.BooleanField(default=False, verbose_name='Студент?')
    is_teacher = models.BooleanField(default=False, verbose_name='Учитель?')
    objects = UserManager()
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user_student')
    student_group = models.ForeignKey(StudentGroup, related_name='student_group', on_delete=models.CASCADE,
                                      verbose_name='Группа', blank=True, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user_teacher')
    student_groups = models.ManyToManyField(StudentGroup, related_name='teacher_group', blank=True)
    bio = models.TextField()
    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'