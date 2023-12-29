
from rest_framework.generics import ListCreateAPIView

from django.shortcuts import render

from .models import BotUser, Survey, MailList
from .serializers import BotUserSerializers, SurveySerializers, MailListSerializer


class BotUserAPIView(ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializers


class SurveyAPIView(ListCreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializers


class MailListAPIView(ListCreateAPIView):
    queryset = MailList.objects.all()
    serializer_class = MailListSerializer


def survey_list(request):
    surveys = Survey.objects.all()
    return render(request, 'survey/survey_list.html', {'surveys': surveys})
