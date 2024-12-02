"""
URL configuration for autism_Emobilis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from my_app import views

urlpatterns = [
    #profiles
    path('api/v1/user/<int:user_id>/create_profile', views.create_profile),  # Profile creation
    path('api/v1/profile',views.profile_list),

    path('api/v1/profile/<int:profile_id>',views.single_user_profile),

    path('api/v1/profile/update/<int:profile_id>',views.update_profile),
    path('api/v1/profile/delete/<int:profile_id>',views.delete_profile),

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

    # Sessions
    path('api/v1/session/create', views.create_session),
    path('api/v1/session', views.session_list),
    path('api/v1/session/<int:session_id>', views.single_session),
    path('api/v1/session/update/<int:session_id>', views.update_session),
    path('api/v1/session/delete/<int:session_id>', views.delete_session),

    # Users
    path('api/v1/user/create', views.create_user),
    path('api/v1/user', views.user_list),
    path('api/v1/user/<int:user_id>', views.single_user),
    path('api/v1/user/update/<int:user_id>', views.update_user),
    path('api/v1/user/delete/<int:user_id>', views.delete_user),

    path('admin/', admin.site.urls),
]
