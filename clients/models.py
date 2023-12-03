from django.db import models
import uuid

class Clients(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    cellphone = models.CharField(max_length=255)
    observation = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)

    user = models.ForeignKey('users.Users', on_delete= models.CASCADE, related_name= 'clients')

