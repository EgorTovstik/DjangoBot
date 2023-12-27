from rest_framework.serializers import ModelSerializer

from .models import BotUser, Survey


class BotUserSerializers(ModelSerializer):
    class Meta:
        model = BotUser
        fields = ('tg_ID', 'name', 'phone_num', 'created_at')


class SurveySerializers(ModelSerializer):
    class Meta:
        model = Survey
        fields = ('tg_ID', 'quest1', 'quest2', 'quest3', 'quest4', 'created_at')

