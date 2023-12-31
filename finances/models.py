from django.db import models
import uuid


class Finances(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    user = models.ForeignKey('users.Users',on_delete=models.CASCADE,related_name='finances')

