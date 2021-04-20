from django.contrib.auth.models import User
from django.db import models


class Topic(models.Model):
    """ Тема обращения """
    title = models.CharField(verbose_name='Тема',
                             max_length=200)
    parent = models.ForeignKey('self',
                               null=True,
                               on_delete=models.CASCADE)


class Department(models.Model):
    """ Подразделение-регистратор обращения """
    title = models.CharField(verbose_name='Подразделение-регистратор',
                             max_length=200)
    parent = models.ForeignKey('self',
                               verbose_name='Головное подразделение',
                               null=True,
                               on_delete=models.SET_NULL)


class Contact(models.Model):
    """
    Контакты консультируемого
    Может быть ФИО, адресом консультируемого, эл.почтой, телефоном
    """
    sni14 = models.CharField(verbose_name='СНИЛС',
                             max_length=14,
                             blank=True)
    fio = models.CharField(max_length=200,
                           verbose_name='Ф.И.О.',
                           blank=True)
    contact = models.JSONField(verbose_name='Контакты')
    created_at = models.DateTimeField(verbose_name="Создано", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Обновлено", auto_now=True)
    edited_by = models.ForeignKey(User,
                                  on_delete=models.SET_NULL)


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
                              on_delete=models.SET_NULL)
    duration = models.IntegerField(verbose_name='Длительность консультации, минут',
                                   null=False)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL)
    advice_type = models.IntegerField(choices=AdviceType.choices,
                                      verbose_name='Тип консультации')
    advice_result = models.IntegerField(verbose_name='Результаты консультирования',
                                        choices=AdviceResult.choices)
    category = models.IntegerField(verbose_name='Физ. или Юр. лицо',
                                   choices=Category.choices)
    contact = models.ForeignKey(Contact,
                                on_delete=models.SET_NULL)
    created_at = models.DateTimeField(verbose_name="Создано",
                                      auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Обновлено",
                                      auto_now=True)
    edited_by = models.ForeignKey(User,
                                  on_delete=models.SET_NULL)


class Note(models.Model):
    """ Примечание к консультации """
    parent = models.ForeignKey('self',
                               null=True,
                               on_delete=models.CASCADE)
    advice = models.ForeignKey(Advice,
                               on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(verbose_name="Создано", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Обновлено", auto_now=True)
    edited_by = models.ForeignKey(User,
                                  on_delete=models.SET_NULL)