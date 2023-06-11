"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from habits import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', views.index, name='home'),
    path('user/<int:pk>', views.user_info, name='user-info'),
    path('profile/<int:pk>', views.profile_details, name="profile-details"),
    path('profile/<int:user_pk>/add', views.profile_add, name="profile-add"),
    path('profile/<int:pk>/edit', views.profile_edit, name='profile-edit'),
    path('tracker/<int:pk>', views.tracker_detail, name='tracker-detail'),
    path('tracker/<int:user_pk>/create',
         views.create_tracker, name='create-tracker'),
    path('tracker/<int:pk>/edit', views.edit_tracker, name='edit-tracker'),
    path('tracker/<int:pk>/delete', views.delete_tracker, name="delete-tracker"),
    path('tracker/<int:pk>/goal',
         views.add_goal_met_data, name='add-goal-met-data'),
    path('tracker/<int:pk>/delete-submission',
         views.delete_submission, name='delete-submission'),
    path('record/<int:pk>/edit-submission',
         views.edit_submission, name="edit-submission"),
]
