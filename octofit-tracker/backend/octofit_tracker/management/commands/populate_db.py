import json
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from pathlib import Path
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        test_data_path = base_dir / 'octofit_tracker/test_data.json'
        with open(test_data_path, 'r') as file:
            data = json.load(file)

        # Populate Users
        for user_data in data['users']:
            User.objects.get_or_create(**user_data)

        # Populate Teams
        for team_data in data['teams']:
            members = team_data.pop('members')
            team, _ = Team.objects.get_or_create(**team_data)
            team.save()
            for member in members:
                user = User.objects.get(username=member)
                team.members.add(user)

        # Populate Activities
        for activity_data in data['activities']:
            user = User.objects.get(username=activity_data.pop('user'))
            duration_parts = activity_data.pop('duration').split(':')
            duration = timedelta(hours=int(duration_parts[0]), minutes=int(duration_parts[1]), seconds=int(duration_parts[2]))
            Activity.objects.get_or_create(user=user, duration=duration, **activity_data)

        # Populate Leaderboard
        for leaderboard_data in data['leaderboard']:
            user = User.objects.get(username=leaderboard_data.pop('user'))
            Leaderboard.objects.get_or_create(user=user, **leaderboard_data)

        # Populate Workouts
        for workout_data in data['workouts']:
            user = User.objects.get(username=workout_data.pop('user'))
            Workout.objects.get_or_create(user=user, **workout_data)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
