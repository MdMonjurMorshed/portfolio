from django.db import models
from datetime import timezone




class Common(models.Model):
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True