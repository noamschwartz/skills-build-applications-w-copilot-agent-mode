from mongoengine import Document, StringField, EmailField, IntField, ListField

class User(Document):
    email = EmailField(required=True, unique=True)
    name = StringField(max_length=255, required=True)
    age = IntField()

class Team(Document):
    name = StringField(max_length=255, required=True)
    members = ListField(EmailField())

class Activity(Document):
    user_email = EmailField(required=True)
    activity_type = StringField(max_length=255, required=True)
    duration = IntField()

class Leaderboard(Document):
    team_name = StringField(max_length=255, required=True)
    points = IntField()

class Workout(Document):
    workout_name = StringField(max_length=255, required=True)
    description = StringField(max_length=1024)