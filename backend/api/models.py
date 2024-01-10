from django.db import models

# Таблица пользователей
class BotUser(models.Model):
    tg_ID = models.CharField(
        max_length=100,
        verbose_name='ID пользователя из телеграмма'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Имя пользователя',
    )
    phone_num = models.CharField(
        max_length=11,
        verbose_name='Номер телефона'
    )

    consent_mail_list = models.TextField(
        verbose_name='Согласие на рассылку',
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.tg_ID} {self.phone_num}'

# Таблица рассылки
class MailList(models.Model):
    text = models.TextField(
        max_length=500,
        verbose_name='Текст рассылки'
    )

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

# Таблица ответы на опрос
class Survey(models.Model):
    tg_ID = models.CharField(
        max_length=100,
        verbose_name='ID пользователя из телеграмма',
        null=True,
    )
    quest1 = models.CharField(
        max_length=100,
        verbose_name='Вопрос 1',
    )
    quest2 = models.CharField(
        max_length=100,
        verbose_name='Вопрос 2',
    )
    quest3 = models.CharField(
        max_length=100,
        verbose_name='Вопрос 3',
    )
    quest4 = models.CharField(
        max_length=100,
        verbose_name='Вопрос 4',
    )
    created_at = models.DateTimeField(
        verbose_name='Дата прохождения',
        auto_now_add=True,
    )

    def __str__(self):
        return f'Прошел {self.tg_ID}, {self.created_at}'

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

