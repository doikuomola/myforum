from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.home, name='home'),
    path('boards/<int:pk>/', views.board_topics, name='board_topics'),
    path('boards/<int:pk>/new_topic', views.new_topic, name='new_topic'),
    
]