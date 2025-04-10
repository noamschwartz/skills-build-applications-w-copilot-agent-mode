from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.conf import settings

class Command(BaseCommand):
    help = 'Initialize MongoDB collections and indexes'

    def handle(self, *args, **kwargs):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']

        # Create collections
        collections = ['users', 'teams', 'activities', 'leaderboard', 'workouts']
        for collection in collections:
            if collection not in db.list_collection_names():
                db.create_collection(collection)
                self.stdout.write(self.style.SUCCESS(f'Created collection: {collection}'))

        # Create indexes
        db.users.create_index([('email', 1)], unique=True)
        db.teams.create_index([('name', 1)], unique=True)
        db.activities.create_index([('user_id', 1), ('date', 1)])
        db.leaderboard.create_index([('team_id', 1), ('period', 1)], unique=True)
        db.workouts.create_index([('type', 1)])

        self.stdout.write(self.style.SUCCESS('Successfully initialized database'))
