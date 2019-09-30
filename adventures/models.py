from django.conf import settings
from django.db import models


class Adventure(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Milestone(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=750)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    adventure = models.ForeignKey("Adventure", on_delete=models.CASCADE)

