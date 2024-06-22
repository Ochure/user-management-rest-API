from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=240)

    def __str__(self):
        return self.name + '' + self.description
