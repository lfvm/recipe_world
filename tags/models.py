from django.db import models


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True,)
    name = models.CharField(max_length = 100, null = False, default="")
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name