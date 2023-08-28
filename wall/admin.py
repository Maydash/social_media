from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from wall.models import Comment, Post


@admin.register(Post)
class CommentAdmin(admin.ModelAdmin):
    """Posts"""
    list_display = ('user', 'create_date', 'moderation', 'published', 'view_count', 'id')
    mptt_level_indent = 15


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    """Comment for Posts"""
    list_display = ('user', 'post', 'created_date', 'update_date', 'published', 'id')
    mptt_level_indent = 15
