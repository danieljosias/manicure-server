from django.db import models
from users.models import Users
import uuid


class Admins(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.OneToOneField(Users, on_delete=models.CASCADE)