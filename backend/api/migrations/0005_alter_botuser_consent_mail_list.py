# Generated by Django 5.0 on 2023-12-29 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_maillist_botuser_consent_mail_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='consent_mail_list',
            field=models.CharField(default='нет', max_length=3, verbose_name='Согласие на рассылку'),
        ),
    ]