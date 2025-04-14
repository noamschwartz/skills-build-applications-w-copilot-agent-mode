from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Add test users
        User(email='john.doe@example.com', name='John Doe', age=30).save()
        User(email='jane.smith@example.com', name='Jane Smith', age=25).save()

        # Add test teams
        Team(name='Team Alpha', members=['john.doe@example.com', 'jane.smith@example.com']).save()

        # Add test activities
        Activity(user_email='john.doe@example.com', activity_type='Running', duration=60).save()
        Activity(user_email='jane.smith@example.com', activity_type='Cycling', duration=45).save()

        # Add test leaderboard
        Leaderboard(team_name='Team Alpha', points=100).save()

        # Add test workouts
        Workout(workout_name='Morning Yoga', description='A relaxing morning yoga session.').save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
