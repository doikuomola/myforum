from django.contrib import admin

from .models import Board, Topic, Post


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    '''Admin View for Topic'''

    list_display = ('board', 'starter', 'subject')
    list_filter = ('board', 'starter', 'subject')
    date_hierarchy = 'last_updated'
    ordering = ('-last_updated',)
