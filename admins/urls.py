from django.urls import path
from .views import AdminView, AdminViewDetail


urlpatterns = [
    path("admins/", AdminView.as_view()),
    path("admins/<admin_id>/", AdminViewDetail.as_view()),
]