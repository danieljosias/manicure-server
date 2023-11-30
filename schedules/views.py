from rest_framework import generics
from .models import Schedule
from .serializers import ScheduleSerializer


class ScheduleView(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    

class ScheduleViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    lookup_url_kwarg = 'schedule_id'