from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    id = models.BigAutoField(primary_key=True,)
    description = models.TextField(null = False)
    title = models.CharField(max_length = 100, null = False, default="")
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.description