from django.db import models
from users.models import CustomUser


class FastPoint(models.Model):
    """ Точка быстрого доступа к приложениям и сайтам """
    class Category(models.IntegerChoices):
        """ Категория точки доступа """
        CTG_SITE = 0, 'Сайт'
        CTG_APP = 1, 'Приложение'
        CTG_PORTAL = 2, 'Портал'

    title = models.CharField(verbose_name='Название',
                             max_length=50)
    description = models.CharField(verbose_name='Описание',
                                   max_length=200,
                                   blank=True)
    url = models.CharField(verbose_name='URL',
                           max_length=200)
    category = models.IntegerField(verbose_name='Категория',
                                   choices=Category.choices)
    created_at = models.DateTimeField(verbose_name="Создано",
                                      auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Обновлено",
                                      auto_now=True)
    edited_by = models.ForeignKey(CustomUser,
                                  null=True,
                                  on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Точка'
        verbose_name_plural = 'Точки'
        ordering = ['title']
