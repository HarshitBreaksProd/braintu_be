from django.db import models

class BrainSpace(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    is_shared = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)