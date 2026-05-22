from django.contrib import admin
from .models import UserProfile, MusicPost, CollaborationRequest, ChatMessage

# 1. User Profile ko Admin me sundar tarike se dikhane ke liye
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'created_at')  # Admin dashboard par ye columns dikhenge
    list_filter = ('role', 'created_at')          # Side me filter karne ka option milega
    search_fields = ('user__username', 'skills', 'bio') # Search bar in fields par kaam karega

# 2. Music & Lyrics Posts ke liye Admin Configuration
@admin.register(MusicPost)
class MusicPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'user__username', 'lyrics')

@admin.register(CollaborationRequest)
class CollaborationRequestAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('sender__username', 'receiver__username', 'message')

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'timestamp', 'is_read')
    list_filter = ('is_read', 'timestamp')
    search_fields = ('sender__username', 'receiver__username', 'message')