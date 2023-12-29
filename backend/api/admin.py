from django.contrib import admin

from .models import BotUser, Survey, MailList


@admin.register(BotUser)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'tg_ID', 'name', 'phone_num', 'consent_mail_list', 'created_at')


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'tg_ID', 'quest1', 'quest2', 'quest3', 'quest4', 'created_at')


@admin.register(MailList)
class MailListAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')

