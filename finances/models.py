from django.db import models
import uuid
from users.models import User


class Finance(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    user = models.OneToOneField(User, on_delete= models.CASCADE)

