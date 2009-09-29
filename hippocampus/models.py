from datetime import datetime

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models


class Visit(models.Model):
    session_key = models.CharField(max_length=255)
    ip_address = models.IPAddressField(blank=True)
    referer = models.URLField(blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=2, blank=True)
    language = models.CharField(max_length=5)
    enter = models.DateTimeField()
    exit = models.DateTimeField(null=True, blank=True)
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    def save(self, *args, **kwargs):
        if not self.id:
            self.enter = datetime.now()
        super(Visit, self).save(*args, **kwargs)


class IPFilter(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.IPAddressField()
    account = models.ForeignKey(User, blank=True, null=True)
