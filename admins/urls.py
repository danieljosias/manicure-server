from django.urls import path
from .views import AdminView


urlpatterns = [
    path("admins/", AdminView.as_view()),
]