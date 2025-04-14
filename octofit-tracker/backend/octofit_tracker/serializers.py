from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    members = serializers.ListField(child=serializers.EmailField())

class ActivitySerializer(serializers.Serializer):
    user_email = serializers.EmailField()
    activity_type = serializers.CharField(max_length=255)
    duration = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    team_name = serializers.CharField(max_length=255)
    points = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    workout_name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=1024)
