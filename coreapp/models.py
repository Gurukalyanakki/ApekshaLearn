from django.db import models
from django.contrib.auth.models import User

class Mentor(models.Model):
    register_number = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def str(self):
        return self.name