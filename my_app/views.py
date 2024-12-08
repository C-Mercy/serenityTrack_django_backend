from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

from my_app.models import Profile, Trigger, Behavior, Intervention, Session, Episode, Therapist, School
from my_app.my_serializers import (
    ProfileSerializer, TriggerSerializer, BehaviorSerializer,
    InterventionSerializer, SessionSerializer, UserSerializer, CustomTokenObtainPairSerializer, EpisodeSerializer,
    SchoolSerializer, TherapistSerializer
)

User = get_user_model()


# Helper for soft delete
def soft_delete(instance):
    instance.is_deleted = True
    instance.save()


# Helper for 404 responses
def handle_not_found(model_name):
    return Response({'error': f'{model_name} not found'}, status=status.HTTP_404_NOT_FOUND)


# USER VIEWS
@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#users
@api_view(['GET'])
@permission_classes([AllowAny])
def user_list(request):
    users = User.objects.filter(is_deleted=False)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])

def single_user(request, user_id):
    user = get_object_or_404(User, id=user_id, is_deleted=False)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['PUT'])

def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id, is_deleted=False)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id, is_deleted=False)
    soft_delete(user)
    return Response({'message': 'User soft-deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# PROFILE VIEWS

@api_view(['POST'])
def create_profile(request):
    user_id = request.data.get('user_id')
    print(f"user_id: {user_id}")
    user = get_object_or_404(User, id=user_id)
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def profile_list(request):
    profiles = Profile.objects.filter(is_deleted=False)
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def single_profile(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id, is_deleted=False)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)


@api_view(['PUT'])
def update_profile(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id, is_deleted=False)
    serializer = ProfileSerializer(profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_profile(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id, is_deleted=False)
    soft_delete(profile)
    return Response({'message': 'Profile soft-deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# TRIGGER VIEWS
@api_view(['POST'])
def create_trigger(request):
    serializer = TriggerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def trigger_list(request):
    triggers = Trigger.objects.filter(is_deleted=False)
    serializer = TriggerSerializer(triggers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def single_trigger(request, trigger_id):
    trigger = get_object_or_404(Trigger, id=trigger_id, is_deleted=False)
    serializer = TriggerSerializer(trigger)
    return Response(serializer.data)


@api_view(['PUT'])
def update_trigger(request, trigger_id):
    trigger = get_object_or_404(Trigger, id=trigger_id, is_deleted=False)
    serializer = TriggerSerializer(trigger, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_trigger(request, trigger_id):
    trigger = get_object_or_404(Trigger, id=trigger_id, is_deleted=False)
    soft_delete(trigger)
    return Response({'message': 'Trigger soft-deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# BEHAVIOR VIEWS
@api_view(['POST'])
def create_behavior(request):
    serializer = BehaviorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def behavior_list(request):
    behaviors = Behavior.objects.filter(is_deleted=False)
    serializer = BehaviorSerializer(behaviors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def single_behavior(request, behavior_id):
    behavior = get_object_or_404(Behavior, id=behavior_id, is_deleted=False)
    serializer = BehaviorSerializer(behavior)
    return Response(serializer.data)


@api_view(['PUT'])
def update_behavior(request, behavior_id):
    behavior = get_object_or_404(Behavior, id=behavior_id, is_deleted=False)
    serializer = BehaviorSerializer(behavior, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_behavior(request, behavior_id):
    behavior = get_object_or_404(Behavior, id=behavior_id, is_deleted=False)
    soft_delete(behavior)
    return Response({'message': 'Behavior soft-deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# INTERVENTION VIEWS
@api_view(['POST'])
def create_intervention(request):
    serializer = InterventionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def intervention_list(request):
    interventions = Intervention.objects.filter(is_deleted=False)
    serializer = InterventionSerializer(interventions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def single_intervention(request, intervention_id):
    intervention = get_object_or_404(Intervention, id=intervention_id, is_deleted=False)
    serializer = InterventionSerializer(intervention)
    return Response(serializer.data)


@api_view(['PUT'])
def update_intervention(request, intervention_id):
    intervention = get_object_or_404(Intervention, id=intervention_id, is_deleted=False)
    serializer = InterventionSerializer(intervention, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_intervention(request, intervention_id):
    intervention = get_object_or_404(Intervention, id=intervention_id, is_deleted=False)
    soft_delete(intervention)
    return Response({'message': 'Intervention soft-deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# SESSION VIEWS
@api_view(['POST'])
def create_session(request):
    serializer = SessionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def session_list(request):
    sessions = Session.objects.filter(is_deleted=False)
    serializer = SessionSerializer(sessions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def single_session(request, session_id):
    session = get_object_or_404(Session, id=session_id, is_deleted=False)
    serializer = SessionSerializer(session)
    return Response(serializer.data)


@api_view(['PUT'])
def update_session(request, session_id):
    session = get_object_or_404(Session, id=session_id, is_deleted=False)
    serializer = SessionSerializer(session, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_session(request, session_id):
    session = get_object_or_404(Session, id=session_id, is_deleted=False)
    soft_delete(session)
    return Response({'message': 'Session soft-deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
# EPISODE VIEWS
@api_view(['POST'])
def create_episode(request):
    serializer = EpisodeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def episode_list(request):
    episodes = Episode.objects.filter(is_deleted=False)
    serializer = EpisodeSerializer(episodes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def single_episode(request, episode_id):
    episode = get_object_or_404(Episode, id=episode_id, is_deleted=False)
    serializer = EpisodeSerializer(episode)
    return Response(serializer.data)


@api_view(['PUT'])
def update_episode(request, episode_id):
    episode = get_object_or_404(Episode, id=episode_id, is_deleted=False)
    serializer = EpisodeSerializer(episode, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_episode(request, episode_id):
    episode = get_object_or_404(Episode, id=episode_id, is_deleted=False)
    soft_delete(episode)
    return Response({'message': 'Episode soft-deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# TOKEN VIEW
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

@api_view(['POST'])
def create_school(request):
    serializer = SchoolSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def school_list(request):
    schools = School.objects.filter(is_deleted=False)
    serializer = SchoolSerializer(schools, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def single_school(request, school_id):
    school = get_object_or_404(School, id=school_id, is_deleted=False)
    serializer = SchoolSerializer(school)
    return Response(serializer.data)

@api_view(['PUT'])
def update_school(request, school_id):
    school = get_object_or_404(School, id=school_id, is_deleted=False)
    serializer = SchoolSerializer(school, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_school(request, school_id):
    school = get_object_or_404(School, id=school_id, is_deleted=False)
    school.is_deleted = True
    school.save()
    return Response({'message': 'School soft-deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_therapist(request):
    serializer = TherapistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def therapist_list(request):
    therapists = Therapist.objects.filter(is_deleted=False)
    serializer = TherapistSerializer(therapists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def single_therapist(request, therapist_id):
    therapist = get_object_or_404(Therapist, id=therapist_id, is_deleted=False)
    serializer = TherapistSerializer(therapist)
    return Response(serializer.data)

@api_view(['PUT'])
def update_therapist(request, therapist_id):
    therapist = get_object_or_404(Therapist, id=therapist_id, is_deleted=False)
    serializer = TherapistSerializer(therapist, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_therapist(request, therapist_id):
    therapist = get_object_or_404(Therapist, id=therapist_id, is_deleted=False)
    therapist.is_deleted = True
    therapist.save()
    return Response({'message': 'Therapist soft-deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
