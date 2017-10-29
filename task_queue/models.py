# -*- coding: utf-8 -*-
"""model of the task queue """
from __future__ import unicode_literals

from django.db import models

# Create your models here.
"""
    common model for message queue record the actors on the bus stats
"""

class Worker(models.Model):
    """model of Worker"""
    worker_id = models.CharField(max_length=32)
    adminState = models.IntegerField()


class Action(models.Model):
    """model for actions"""
    action_id = models.CharField(max_length=32)
    action_name = models.CharField(max_length=32)


class Task(models.Model):
    """model of Task"""
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    reference = models.CharField(max_length=20)
   

    