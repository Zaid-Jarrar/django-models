from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Snack(models.Model):
    name = models.CharField(max_length=64)
    # to link here between purchaser and another model user model, when it deletes the user is deleted as well
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name