from django.urls import path

from .views import BotUserAPIView, SurveyAPIView

urlpatterns = [
    path('bot-users', BotUserAPIView.as_view(), name='Пользователи'),
    path('surveys', SurveyAPIView.as_view(), name='Опросы'),
]