from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.models import Team, Activity, Leaderboard, Workout
import json
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Load test data
        data_file = os.path.join(settings.BASE_DIR, 'octofit_tracker', 'test_data.json')
        with open(data_file, 'r') as f:
            test_data = json.load(f)

        # Create users
        self.stdout.write('Creating users...')
        users = {}
        for user_data in test_data['users']:
            user = User.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name']
            )
            users[user.username] = user

        # Create teams
        self.stdout.write('Creating teams...')
        teams = {}
        for team_data in test_data['teams']:
            team = Team.objects.create(
                name=team_data['name'],
                description=team_data['description']
            )
            for username in team_data['members']:
                team.members.add(users[username])
            teams[team.name] = team

        # Create activities
        self.stdout.write('Creating activities...')
        for activity_data in test_data['activities']:
            Activity.objects.create(
                user=users[activity_data['username']],
                type=activity_data['type'],
                duration=activity_data['duration'],
                distance=activity_data['distance'],
                calories=activity_data['calories'],
                notes=activity_data['notes']
            )

        # Create workouts
        self.stdout.write('Creating workouts...')
        for workout_data in test_data['workouts']:
            Workout.objects.create(**workout_data)

        # Create leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        for leaderboard_data in test_data['leaderboard']:
            Leaderboard.objects.create(
                team=teams[leaderboard_data['team']],
                period=leaderboard_data['period'],
                points=leaderboard_data['points']
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated database'))
