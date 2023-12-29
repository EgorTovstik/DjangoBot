from django.urls import path

from .views import BotUserAPIView, SurveyAPIView, survey_list, MailListAPIView

urlpatterns = [
    path('bot-users', BotUserAPIView.as_view(), name='Пользователи'),
    path('surveys', SurveyAPIView.as_view(), name='Опросы'),
    path('mail-list', MailListAPIView.as_view(), name='Рассылка'),
    path('', survey_list, name='home')
]