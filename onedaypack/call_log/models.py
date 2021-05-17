from django.contrib.auth.models import User
from django.db import models

from users.models import CustomUser


class Topic(models.Model):
    """ Тема обращения """
    title = models.CharField(verbose_name='Название',
                             max_length=200)
    parent = models.ForeignKey('self',
                               null=True,
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['title']


class Department(models.Model):
    """ Подразделение-регистратор обращения """
    title = models.CharField(verbose_name='Подразделение-регистратор',
                             max_length=200)
    parent = models.ForeignKey('self',
                               verbose_name='Головное подразделение',
                               null=True,
                               on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
        ordering = ['title']


class Contact(models.Model):
    """
    Контакты консультируемого
    Может быть ФИО, адресом консультируемого, эл.почтой, телефоном
    """
    sni14 = models.CharField(verbose_name='СНИЛС',
                             max_length=14,
                             blank=True,
                             default='123-456-789 00')
    fio = models.CharField(max_length=200,
                           verbose_name='Ф.И.О.',
                           blank=True,
                           default='')
    contact = models.JSONField(verbose_name='Контакты',
                               null=True)
    created_at = models.DateTimeField(verbose_name="Создано",
                                      auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Обновлено",
                                      auto_now=True)
    edited_by = models.ForeignKey(CustomUser,
                                  verbose_name="Редактор",
                                  null=True,
                                  on_delete=models.SET_NULL)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['-updated_at']


class Advice(models.Model):
    """ Обращение за консультацией гражданина или организации """

    class AdviceType(models.IntegerChoices):
        """ Вид консультации """
        COMMON_QUESTION = 1, '01 Общие вопросы в компетенции ПФР'
        PRIVATE_QUESTION = 2, '02 Вопросам с предоставлением персональной информации' \
                              ' и использованием «кодового слова»'

    class AdviceResult(models.IntegerChoices):
        """Результаты консультирования"""
        RESULT_01 = 1, '01 Представлена консультация'
        RESULT_02 = 2, '02 Гражданин записан на прием в ТО ПФР'
        RESULT_03 = 3, '03 Звонок переведен на специалиста ПФР'
        RESULT_04 = 4, '04 Гражданину предложено подготовить письменное обращение'
        RESULT_05 = 5, '05 Планируется обратная связь с гражданином(исходящее информирование)'
        RESULT_06 = 6, '06 Осуществлена запись для выезда специалиста КС на дом'
        RESULT_07 = 7, '07 Осуществлена запись о предварительном заказе документов'

    class Category(models.IntegerChoices):
        """ Физ. или Юр. лицо """
        CTG_PERSON = 0, '0 Физическое лицо'
        CTG_COMPANY = 1, '1 Юридическое лицо'

    topic = models.ForeignKey(Topic,
                              verbose_name='Тема',
                              null=True,
                              on_delete=models.SET_NULL)
    duration = models.IntegerField(verbose_name='Длительность консультации, минут')
    department = models.ForeignKey(Department,
                                   null=True,
                                   on_delete=models.SET_NULL)
    advice_type = models.IntegerField(choices=AdviceType.choices,
                                      verbose_name='Тип консультации')
    advice_result = models.IntegerField(verbose_name='Результаты консультирования',
                                        choices=AdviceResult.choices)
    category = models.IntegerField(verbose_name='Физ. или Юр. лицо',
                                   choices=Category.choices)
    contact = models.ForeignKey(Contact,
                                null=True,
                                on_delete=models.SET_NULL)
    created_at = models.DateTimeField(verbose_name="Создано",
                                      auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Обновлено",
                                      auto_now=True)
    edited_by = models.ForeignKey(CustomUser,
                                  null=True,
                                  on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
        ordering = ['-updated_at']


class Note(models.Model):
    """ Примечание к консультации """
    parent = models.ForeignKey('self',
                               null=True,
                               on_delete=models.CASCADE)
    advice = models.ForeignKey(Advice,
                               on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(verbose_name="Создано",
                                      auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Обновлено",
                                      auto_now=True)
    edited_by = models.ForeignKey(CustomUser,
                                  null=True,
                                  on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Примечание'
        verbose_name_plural = 'Примечания'
        ordering = ['-created_at']
