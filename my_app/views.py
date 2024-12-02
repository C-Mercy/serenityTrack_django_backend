from http import HTTPStatus

from django.contrib.auth import get_user_model

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from autism_Emobilis import settings
from my_app.models import Profile, Trigger, Behavior, Intervention, Session
from my_app.my_serializers import ProfileSerializer, TriggerSerializer, BehaviorSerializer, InterventionSerializer, \
    SessionSerializer, UserSerializer


# Create your views here.
#PROFILE
@api_view(['POST'])
def create_profile(request, user_id):
    """
    Create a profile for the given user.
    """
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    # Extract specific fields from the request data
    profile_data = request.data
    first_name = profile_data.get('first_name')
    last_name = profile_data.get('last_name')
    date_of_birth = profile_data.get('date_of_birth')  # Explicitly extract date_of_birth
    diagnosis_date = profile_data.get('diagnosis_date')
    severity = profile_data.get('severity')
    communication_level = profile_data.get('communication_level')
    created_at = profile_data.get('created_at')
    updated_at = profile_data.get('updated_at')

    if not date_of_birth:
        return Response({'error': 'Date of birth is required'}, status=status.HTTP_400_BAD_REQUEST)

    # Create Profile associated with this user
    Profile.objects.create(
        user=user,
        first_name=first_name,
        last_name=last_name,
        date_of_birth=date_of_birth,
        diagnosis_date=diagnosis_date,
        severity=severity,
        communication_level=communication_level,
        created_at=created_at,
        updated_at=updated_at
    )

    return Response({'message': 'Profile created successfully'}, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def profile_list(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)




@api_view(['GET'])
def single_user_profile(request,profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)


@api_view(['PUT'])
def update_profile(request,profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    serializer = ProfileSerializer(profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=HTTPStatus.BAD_REQUEST)


@api_view(['DELETE'])
def delete_profile(request,profile_id):
   try:
       profile = Profile.objects.get(id=profile_id,is_deleted=False)
       profile.delete()
       return Response({'message': 'Profile soft-deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
   except Profile.DoesNotExist:
       return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)



# TRIGGER
@api_view(['POST'])
def create_trigger(request):
    serializer = TriggerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def trigger_list(request):
    triggers = Trigger.objects.all()
    serializer = TriggerSerializer(triggers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def single_trigger(request, trigger_id):
    try:
        trigger = Trigger.objects.get(id=trigger_id, is_deleted=False)
        serializer = TriggerSerializer(trigger)
        return Response(serializer.data)
    except Trigger.DoesNotExist:
        return Response({'error': 'Trigger not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_trigger(request, trigger_id):
    try:
        trigger = Trigger.objects.get(id=trigger_id, is_deleted=False)
    except Trigger.DoesNotExist:
        return Response({'error': 'Trigger not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TriggerSerializer(trigger, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_trigger(request, trigger_id):
    try:
        trigger = Trigger.objects.get(id=trigger_id, is_deleted=False)
        trigger.delete()  # Marks `is_deleted` as True
        return Response({'message': 'Trigger soft-deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Trigger.DoesNotExist:
        return Response({'error': 'Trigger not found'}, status=status.HTTP_404_NOT_FOUND)

#BEHAVIUOR
@api_view(['POST'])
def create_behavior(request):
    serializer = BehaviorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def behavior_list(request):
    behaviors = Behavior.objects.all()
    serializer = BehaviorSerializer(behaviors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def single_behavior(request, behavior_id):
    try:
        behavior = Behavior.objects.get(id=behavior_id, is_deleted=False)
        serializer = BehaviorSerializer(behavior)
        return Response(serializer.data)
    except Behavior.DoesNotExist:
        return Response({'error': 'Behavior not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_behavior(request, behavior_id):
    try:
        behavior = Behavior.objects.get(id=behavior_id, is_deleted=False)
    except Behavior.DoesNotExist:
        return Response({'error': 'Behavior not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BehaviorSerializer(behavior, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_behavior(request, behavior_id):
    try:
        behavior = Behavior.objects.get(id=behavior_id, is_deleted=False)
        behavior.delete()
        return Response({'message': 'Behavior soft-deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Behavior.DoesNotExist:
        return Response({'error': 'Behavior not found'}, status=status.HTTP_404_NOT_FOUND)


#INTERVENTION
@api_view(['POST'])
def create_intervention(request):
    serializer = InterventionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def intervention_list(request):
    Interventions = Intervention.objects.all()
    serializer = InterventionSerializer(Interventions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def single_intervention(request, intervention_id):
    try:
        intervention = Intervention.objects.get(id=intervention_id, is_deleted=False)
        serializer = InterventionSerializer(intervention)
        return Response(serializer.data)
    except Intervention.DoesNotExist:
        return Response({'error': 'Intervention not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_intervention(request, intervention_id):
    try:
        intervention = Intervention.objects.get(id=intervention_id, is_deleted=False)
    except Intervention.DoesNotExist:
        return Response({'error': 'Intervention not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = InterventionSerializer(intervention, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_intervention(request, intervention_id):
    try:
        intervention = Intervention.objects.get(id=intervention_id, is_deleted=False)
        intervention.delete()
        return Response({'message': 'Intervention soft-deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Intervention.DoesNotExist:
        return Response({'error': 'Intervention not found'}, status=status.HTTP_404_NOT_FOUND)

#Session
@api_view(['POST'])
def create_session(request):
    serializer = SessionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#SESSIONS
@api_view(['GET'])
def session_list(request):
    """
    Get a list of all non-deleted sessions.
    """
    sessions = Session.objects.filter(is_deleted=False)
    serializer = SessionSerializer(sessions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def single_session(request, session_id):
    """
    Get details of a single session by ID.
    """
    try:
        session = Session.objects.get(id=session_id, is_deleted=False)
        serializer = SessionSerializer(session)
        return Response(serializer.data)
    except Session.DoesNotExist:
        return Response({'error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_session(request, session_id):
    """
    Update a session by ID.
    """
    try:
        session = Session.objects.get(id=session_id, is_deleted=False)
    except Session.DoesNotExist:
        return Response({'error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = SessionSerializer(session, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_session(request, session_id):
    """
    Soft delete a session by ID.
    """
    try:
        session = Session.objects.get(id=session_id, is_deleted=False)
        session.delete()  # Marks is_deleted=True
        return Response({'message': 'Session soft-deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Session.DoesNotExist:
        return Response({'error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)


#USERS


User = get_user_model()

@api_view(['GET'])
def user_list(request):
    """
    Get a list of all non-deleted users.
    """
    users = User.objects.filter(is_deleted=False)  # Should work with the model
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def single_user(request, user_id):
    """
    Get details of a single user by ID.
    """
    try:
        user = User.objects.get(id=user_id, is_deleted=False)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_user(request):
    """
    Create a new user and an associated profile.
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()  # This will create the user
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user(request, user_id):
    """
    Update a user by ID.
    """
    try:
        user = User.objects.get(id=user_id, is_deleted=False)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request, user_id):
    """
    Soft delete a user by ID.
    """
    try:
        user = User.objects.get(id=user_id, is_deleted=False)
        user.delete()  # Marks is_deleted=True
        return Response({'message': 'User soft-deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

