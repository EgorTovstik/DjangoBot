from rest_framework.serializers import ModelSerializer

from .models import BotUser, Survey, MailList


class BotUserSerializers(ModelSerializer):
    class Meta:
        model = BotUser
        fields = ('tg_ID', 'name', 'phone_num', 'consent_mail_list', 'created_at')


class MailListSerializer(ModelSerializer):
    class Meta:
        model = MailList
        fields = ('id', 'text')


class SurveySerializers(ModelSerializer):
    class Meta:
        model = Survey
        fields = ('tg_ID', 'quest1', 'quest2', 'quest3', 'quest4', 'created_at')

