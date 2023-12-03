from rest_framework import generics
from .models import Admins
from .serializers import AdminSerializer


class AdminView(generics.ListCreateAPIView):
    queryset = Admins.objects.all()
    serializer_class = AdminSerializer

