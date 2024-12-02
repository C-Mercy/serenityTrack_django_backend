from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile, Trigger, Behavior, Intervention, Session

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password', 'user_type']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            user_type=validated_data['user_type']  # User type field
        )
        return user



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [ 'user','id', 'first_name', 'last_name', 'date_of_birth',
                   'diagnosis_date', 'severity', 'communication_level', 'created_at', 'updated_at' ]
        read_only_fields = ['created_at', 'updated_at']

class TriggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trigger
        fields = ['id', 'profile', 'trigger_type', 'description', 'severity', 'management_strategy','created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at','id']

class BehaviorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Behavior
        fields = ['id', 'profile', 'behavior_type', 'description', 'frequency', 'context','created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at','id']

class InterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervention
        fields = ['id', 'behavior', 'intervention_type', 'description', 'effectiveness','created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at','id']

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'profile', 'session_date', 'therapist', 'notes', 'goals','created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at','id']