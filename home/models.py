# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Employee(models.Model):

    #__Employee_FIELDS__
    fio = models.TextField(max_length=255, null=True, blank=True)
    pl = models.TextField(max_length=255, null=True, blank=True)
    position = models.TextField(max_length=255, null=True, blank=True)

    #__Employee_FIELDS__END

    class Meta:
        verbose_name        = _("Employee")
        verbose_name_plural = _("Employee")


class System(models.Model):

    #__System_FIELDS__
    description = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__System_FIELDS__END

    class Meta:
        verbose_name        = _("System")
        verbose_name_plural = _("System")


class Incident(models.Model):

    #__Incident_FIELDS__
    description = models.TextField(max_length=255, null=True, blank=True)
    asignee = models.CharField(max_length=255, null=True, blank=True)

    #__Incident_FIELDS__END

    class Meta:
        verbose_name        = _("Incident")
        verbose_name_plural = _("Incident")



#__MODELS__END
