from django.db import models
from django.urls import reverse


class Wackywidgets(models.Model):
    description = models.TextField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'wackywidgets_id': self.id})

