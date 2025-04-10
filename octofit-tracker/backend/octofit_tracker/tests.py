from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password")
        self.assertEqual(user.username, "testuser")

class TeamModelTest(TestCase):
    def test_team_creation(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password")
        team = Team.objects.create(name="Test Team")
        team.members.add(user)
        self.assertEqual(team.name, "Test Team")

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password")
        activity = Activity.objects.create(user=user, activity_type="Running", duration="01:00:00")
        self.assertEqual(activity.activity_type, "Running")

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password")
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password")
        workout = Workout.objects.create(user=user, workout_type="Yoga", calories_burned=200.5, date="2025-04-10")
        self.assertEqual(workout.workout_type, "Yoga")