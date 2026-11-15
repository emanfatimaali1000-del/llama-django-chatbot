from django.contrib import admin
from .models import ChatSession, Message


@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'user', 'created_at', 'updated_at')

    search_fields = ('title', 'user__username')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):

    list_display = ('id', 'chat', 'role', 'created_at')

    list_filter = ('role', 'created_at')