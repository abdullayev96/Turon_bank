from django.db import models
from django.conf import settings

# CustomUser = settings.AUTH_USER_MODEL

class BaseModel(models.Model):
    created_at = models.DateField(blank=False)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True

