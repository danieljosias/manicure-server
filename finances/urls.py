from django.urls import path
from .views import FinanceView, FinanceViewDetail


urlpatterns = [
    path("finances/", FinanceView.as_view()),
    path("finances/<finance_id>/", FinanceViewDetail.as_view()),
]