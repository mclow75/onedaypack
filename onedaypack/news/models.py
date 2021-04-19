from django.db import models


class Notice(models.Model):
    """ Заметка для ленты и раздела новости"""
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    content = models.TextField(verbose_name="Содержание")
    created_at = models.DateTimeField(verbose_name="Создано", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Обновлено", auto_now=True)
    photo = models.ImageField(verbose_name="Фотография", upload_to="photos/%Y/%m/%d")
    is_published = models.BooleanField(verbose_name="Опубликовать", default=True)
