from rest_framework import generics
from .models import Finances
from .serializers import FinanceSerializer


class FinanceView(generics.ListCreateAPIView):
    queryset = Finances.objects.all()
    serializer_class = FinanceSerializer
    

class FinanceViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Finances.objects.all()
    serializer_class = FinanceSerializer

    lookup_url_kwarg = 'finance_id'