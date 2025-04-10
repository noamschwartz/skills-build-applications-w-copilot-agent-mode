from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.team = Team.objects.create(name='Test Team', description='Test Description')
        self.team.members.add(self.user)
        
    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.members.count(), 1)

    def test_activity_creation(self):
        activity = Activity.objects.create(
            user=self.user,
            type='running',
            duration=30,
            distance=5.0,
            calories=300
        )
        self.assertEqual(activity.type, 'running')
        self.assertEqual(activity.user, self.user)

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(
            team=self.team,
            period='weekly',
            points=100
        )
        self.assertEqual(leaderboard.team, self.team)
        self.assertEqual(leaderboard.points, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(
            name='Test Workout',
            type='cardio',
            difficulty='intermediate',
            description='Test workout description',
            duration=45,
            calories_burn=400
        )
        self.assertEqual(workout.name, 'Test Workout')
        self.assertEqual(workout.difficulty, 'intermediate')

class APITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.team = Team.objects.create(name='Test Team', description='Test Description')
        
    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)

    def test_team_list(self):
        response = self.client.get(reverse('team-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_activity(self):
        url = reverse('activity-list')
        data = {
            'type': 'running',
            'duration': 30,
            'distance': 5.0,
            'calories': 300
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Activity.objects.count(), 1)

    def test_workout_list(self):
        Workout.objects.create(
            name='Test Workout',
            type='cardio',
            difficulty='intermediate',
            description='Test workout description',
            duration=45,
            calories_burn=400
        )
        response = self.client.get(reverse('workout-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)