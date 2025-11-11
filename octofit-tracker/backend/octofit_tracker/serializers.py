from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

# Custom field to handle MongoDB ObjectId (read-only to avoid write errors)
class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)
    
    def to_internal_value(self, data):
        # Not used in input since field is read_only, but keep for completeness
        return data

class UserSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    
    class Meta:
        model = User
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    
    class Meta:
        model = Team
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    
    class Meta:
        model = Activity
        fields = '__all__'

class LeaderboardSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    
    class Meta:
        model = Workout
        fields = '__all__'
