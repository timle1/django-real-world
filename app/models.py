from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Speaker(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=50)
    bio = models.TextField(max_length=1000)
    twitter = models.CharField(max_length=16, blank=True)
    facebook = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Track(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

SESSION_STATUSES = (
    ('a', 'Approved'),
    ('s', 'Submitted'),
    ('r', 'Rejected'),
)
class Session(models.Model):
    title = models.CharField(max_length=50)
    abstract = models.TextField(max_length=2000)
    track = models.ForeignKey(Track)
    speaker = models.ForeignKey(Speaker)
    status = models.CharField(max_length=1, choices=SESSION_STATUSES, default='s')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('session-detail', kwargs={'pk': self.pk})