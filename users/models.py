from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Users(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)




