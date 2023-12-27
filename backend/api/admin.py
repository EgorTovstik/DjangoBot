from django.contrib import admin

from .models import BotUser, Survey


@admin.register(BotUser)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'tg_ID', 'name', 'phone_num', 'created_at')


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'tg_ID', 'quest1', 'quest2', 'quest3', 'quest4', 'created_at')
