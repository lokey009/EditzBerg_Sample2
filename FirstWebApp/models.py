from django.db import models

# Create your models here.


# myapp/models.py
from django.db import models

class UserData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
