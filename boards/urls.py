from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.home, name='home'),
    path('boards/<int:pk>/', views.board_topics, name='board_topics'),
    path('boards/<int:pk>/new_topic', views.new_topic, name='new_topic'),
    path('boards/<int:pk>/topics/<topic_pk>/', views.topic_posts, name='topic_posts'),
    path('boards/<int:pk>/topics/<topic_pk>/reply/', views.reply_topic, name='reply_topic'),
]