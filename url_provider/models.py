from django.db import models

# Create your models here.
class UserDescription(models.Model):

    username = models.CharField(max_length=200,null=True)
    title = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=100000,null=True)

    def __str__(self):
        return self.title
