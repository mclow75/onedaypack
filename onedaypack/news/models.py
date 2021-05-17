from django.db import models
from users.models import CustomUser


class Notice(models.Model):
    """ Заметка для ленты и раздела новости"""
    title = models.CharField(verbose_name="Заголовок",
                             max_length=200)
    content = models.TextField(verbose_name="Содержание")
    created_at = models.DateTimeField(verbose_name="Создано",
                                      auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Обновлено",
                                      auto_now=True)
    photo = models.ImageField(verbose_name="Фотография",
                              upload_to="photos/%Y/%m/%d",
                              blank=True)
    is_published = models.BooleanField(verbose_name="Опубликовано",
                                       default=True)
    edited_by = models.ForeignKey(CustomUser,
                                  null=True,
                                  on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.title
