from django.contrib.auth.models import User
import datetime
from django.utils import timezone

from django.db import models

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, editable=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_added <= now
    recently.admin_order_field = 'date_added'
    recently.boolean = True
    recently.short_description = 'Publicação Recente?'
