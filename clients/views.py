from rest_framework import generics
from .models import Clients
from .serializers import ClientSerializer


class ClientView(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    

class ClientViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer

    lookup_url_kwarg = 'client_id'
