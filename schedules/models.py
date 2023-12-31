from django.db import models
import uuid


class Schedules(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    cellphone = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    hour = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

    user = models.ForeignKey('users.Users', on_delete= models.CASCADE, related_name= 'schedules')


