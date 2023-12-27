
from rest_framework.generics import ListCreateAPIView

from .models import BotUser, Survey
from .serializers import BotUserSerializers, SurveySerializers


class BotUserAPIView(ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializers


class SurveyAPIView(ListCreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializers

