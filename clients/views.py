from rest_framework import generics
from .models import Clients
from .serializers import ClientSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class ClientView(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer 

class ClientViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer

    lookup_url_kwarg = 'client_id'

    
