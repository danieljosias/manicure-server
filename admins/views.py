from rest_framework import generics
from .models import Admin
from .serializers import AdminSerializer


class AdminView(generics.ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

