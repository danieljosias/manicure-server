from rest_framework import generics
from .models import Schedules
from .serializers import ScheduleSerializer


class ScheduleView(generics.ListCreateAPIView):
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer
    

class ScheduleViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer

    lookup_url_kwarg = 'schedule_id'