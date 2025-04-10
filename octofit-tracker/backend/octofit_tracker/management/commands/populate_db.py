from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from pymongo import MongoClient
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Insert test data
        users = [
            {"_id": 1, "username": "john_doe", "email": "john@example.com"},
            {"_id": 2, "username": "jane_doe", "email": "jane@example.com"}
        ]
        db.users.insert_many(users)

        teams = [
            {"_id": 1, "name": "Team A", "members": [1, 2]},
        ]
        db.teams.insert_many(teams)

        activities = [
            {"_id": 1, "user_id": 1, "activity_type": "Running", "duration": 30, "date": datetime.now()},
        ]
        db.activity.insert_many(activities)

        leaderboard = [
            {"_id": 1, "user_id": 1, "score": 100},
        ]
        db.leaderboard.insert_many(leaderboard)

        workouts = [
            {"_id": 1, "user_id": 1, "workout_type": "Cardio", "date": datetime.now()},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
