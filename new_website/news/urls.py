from django.urls import path
from .views import news_list, add_news

urlpatterns = [
    path('', news_list, name='news_list'),
    path('add/', add_news, name='add_news'),
]