from rest_framework import generics
from .models import Finance
from .serializers import FinanceSerializer


class FinanceView(generics.ListCreateAPIView):
    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer
    

class FinanceViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer

    lookup_url_kwarg = 'finance_id'