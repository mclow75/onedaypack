from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    middle_name = models.CharField(verbose_name="Отчество",
                                   max_length=150,
                                   blank=True)
    birthday = models.DateField(verbose_name="Дата рождения",
                                null=True)

    class Meta:
        app_label = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
