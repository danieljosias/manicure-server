from django.urls import path
from .views import ScheduleView, ScheduleViewDetail


urlpatterns = [
    path("schedules/", ScheduleView.as_view()),
    path("schedules/<schedule_id>/", ScheduleViewDetail.as_view())
]