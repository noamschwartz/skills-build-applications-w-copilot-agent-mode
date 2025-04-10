from django.contrib import admin
from .models import Team, Activity, Leaderboard, Workout

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'duration', 'date')
    list_filter = ('type', 'date')
    search_fields = ('user__username', 'type')

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('team', 'period', 'points', 'last_updated')
    list_filter = ('period',)
    search_fields = ('team__name',)

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'difficulty', 'duration')
    list_filter = ('difficulty', 'type')
    search_fields = ('name', 'type')