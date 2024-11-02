from django.urls import path
from .views import task_view, team_member_details

urlpatterns=[
    path('', task_view, name='task_view'),
    path('get-team-member-details/', team_member_details, name='get_team_member_details'),

]