from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('chat/', views.chat, name='chat'),

    path('new-chat/', views.create_chat, name='create_chat'),

    path(
        'history/<int:chat_id>/',
        views.get_messages,
        name='get_messages'
    ),

    path(
        'delete-chat/<int:chat_id>/',
        views.delete_chat,
        name='delete_chat'
    ),

]