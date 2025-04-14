from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

class UserListView(APIView):
    def get(self, request):
        return Response({'message': 'List of users'})

class TeamListView(APIView):
    def get(self, request):
        return Response({'message': 'List of teams'})

class ActivityListView(APIView):
    def get(self, request):
        return Response({'message': 'List of activities'})

class LeaderboardListView(APIView):
    def get(self, request):
        return Response({'message': 'Leaderboard'})

class WorkoutListView(APIView):
    def get(self, request):
        return Response({'message': 'List of workouts'})

@api_view(['GET'])
def api_root(request):
    return Response({'message': 'API Root'})