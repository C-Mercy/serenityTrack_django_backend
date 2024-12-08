from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Profile, Trigger, Behavior, Intervention, Session, Episode, School, Therapist


class UserSerializer(serializers.ModelSerializer):
    profiles = serializers.SerializerMethodField()  # Fetch related profiles

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'user_type', 'profiles']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
            user_type=validated_data['user_type']  # User type field
        )
        return user

    def get_profiles(self, obj):
        profiles = obj.profiles.all()  # Assumes related_name='profiles' in the Profile model
        return ProfileSerializer(profiles, many=True).data


class CustomTokenObtainPairSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if user is None:
            raise serializers.ValidationError('Invalid credentials')

        refresh = RefreshToken.for_user(user)

        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': UserSerializer(user).data
        }


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class TriggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trigger
        fields = ['id', 'profile','episode', 'trigger_type', 'description', 'severity', 'management_strategy', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'id']


class BehaviorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Behavior
        fields = ['id', 'profile', 'behavior_type', 'description','episode', 'frequency', 'context', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'id']


class InterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervention
        fields = ['id', 'behavior','profile', 'episode','intervention_type', 'description', 'effectiveness', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'id']




class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['id', 'profile', 'title', 'description','start_time', 'end_time', 'episode_date', 'duration', 'is_deleted', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'id']

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'profile', 'session_date', 'therapist', 'notes', 'goals', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'id']
class ProfileSerializer(serializers.ModelSerializer):
    triggers = TriggerSerializer(many=True, read_only=True)
    behaviors = BehaviorSerializer(many=True, read_only=True)
    sessions = SessionSerializer(many=True, read_only=True)
    interventions = InterventionSerializer(many=True, read_only=True)
    episodes = EpisodeSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'first_name', 'last_name', 'date_of_birth', 'diagnosis_date', 'severity',
                  'communication_level', 'created_at', 'updated_at', 'triggers', 'behaviors', 'sessions','episodes','interventions']
        read_only_fields = ['created_at', 'updated_at']

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class TherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        fields = '__all__'
