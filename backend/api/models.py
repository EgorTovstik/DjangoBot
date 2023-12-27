from django.db import models


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

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.tg_ID} {self.phone_num}'


class Survey(models.Model):
    tg_ID = models.TextField(
        max_length=100,
        verbose_name='ID пользователя из телеграмма',
        null=True
    )
    quest1 = models.TextField(
        verbose_name='Вопрос 1',
    )
    quest2 = models.TextField(
        verbose_name='Вопрос 2',
    )
    quest3 = models.TextField(
        verbose_name='Вопрос 3',
    )
    quest4 = models.TextField(
        verbose_name='Вопрос 4',
    )
    created_at = models.DateTimeField(
        verbose_name='Дата прохождения',
        auto_now_add=True,
    )

    def __str__(self):
        return f'Прошел {self.pk}, {self.created_at}'

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

