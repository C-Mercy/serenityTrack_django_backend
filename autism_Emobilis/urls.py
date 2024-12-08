from django.contrib import admin
from django.urls import path

from my_app import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

from my_app.views import CustomTokenObtainPairView

urlpatterns = [
    # Login
    path('api/token/login', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/logout/', TokenBlacklistView.as_view(), name='token_blacklist'),

    # Profiles
    path('api/v1/create_profile', views.create_profile),
    path('api/v1/profile', views.profile_list),
    path('api/v1/profile/<int:profile_id>', views.single_profile),
    path('api/v1/profile/update/<int:profile_id>', views.update_profile),
    path('api/v1/profile/delete/<int:profile_id>', views.delete_profile),

    # Triggers
    path('api/v1/trigger/create', views.create_trigger),
    path('api/v1/trigger', views.trigger_list),
    path('api/v1/trigger/<int:trigger_id>', views.single_trigger),
    path('api/v1/trigger/update/<int:trigger_id>', views.update_trigger),
    path('api/v1/trigger/delete/<int:trigger_id>', views.delete_trigger),

    # Behaviors
    path('api/v1/behavior/create', views.create_behavior),
    path('api/v1/behavior', views.behavior_list),
    path('api/v1/behavior/<int:behavior_id>', views.single_behavior),
    path('api/v1/behavior/update/<int:behavior_id>', views.update_behavior),
    path('api/v1/behavior/delete/<int:behavior_id>', views.delete_behavior),

    # Interventions
    path('api/v1/intervention/create', views.create_intervention),
    path('api/v1/intervention', views.intervention_list),
    path('api/v1/intervention/<int:intervention_id>', views.single_intervention),
    path('api/v1/intervention/update/<int:intervention_id>', views.update_intervention),
    path('api/v1/intervention/delete/<int:intervention_id>', views.delete_intervention),

    # Episodes
    path('api/v1/episode/create', views.create_episode),
    path('api/v1/episode', views.episode_list),
    path('api/v1/episode/<int:episode_id>', views.single_episode),
    path('api/v1/episode/update/<int:episode_id>', views.update_episode),
    path('api/v1/episode/delete/<int:episode_id>', views.delete_episode),

    # Users
    path('api/v1/user/create', views.create_user),
    path('api/v1/user', views.user_list),
    path('api/v1/user/<int:user_id>', views.single_user),
    path('api/v1/user/update/<int:user_id>', views.update_user),
    path('api/v1/user/delete/<int:user_id>', views.delete_user),

#session
    path('api/v1/user/delete/<int:session_id>', views.delete_session),
    path('api/v1/session/create', views.create_session),
    path('api/v1/session', views.session_list),
    path('api/v1/session/<int:session_id>', views.single_session),
    path('api/v1/session/update/<int:session_id>', views.update_session),


    #school
    path('api/v1/school/', views.school_list, name='school_list'),
    path('api/v1/school/create', views.create_school, name='create_school'),
    path('api/v1/school/<int:school_id>', views.single_school, name='single_school'),
    path('api/v1/school/update/<int:school_id>', views.update_school, name='update_school'),
    path('api/v1/school/delete/<int:school_id>', views.delete_school, name='delete_school'),

   #therapists
    path('api/v1/therapist/', views.therapist_list, name='therapist_list'),
    path('api/v1/therapist/create', views.create_therapist, name='create_therapist'),
    path('api/v1/therapist/<int:theraist_id>', views.single_therapist, name='single_therapist'),
    path('api/v1/therapist/update/<int:therapist_id>', views.update_therapist, name='update_therapist'),
    path('api/v1/therapist/delete/<int:therapist_id>', views.delete_therapist, name='delete_therapist'),


path('admin/', admin.site.urls),
]
