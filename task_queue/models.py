# -*- coding: utf-8 -*-
"""model of the task queue """
from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
"""
    common model for message queue record the actors on the bus stats
"""
@python_2_unicode_compatible
class Worker(models.Model):
    """model of Worker"""
    worker_id = models.CharField(max_length=32)
    location = models.GenericIPAddressField()
    worker_name = models.CharField(max_length=32)
    def str(self):
        """decorate required"""
        return self.worker_name

    def __str__(self):
        return self.worker_name

@python_2_unicode_compatible 
class Action(models.Model):
    """model for actions"""
    action_id = models.CharField(max_length=32)
    action_name = models.CharField(max_length=32)
    def str(self):
        """decorator string """
        return self.__str__()

    def __str__(self):
        return self.action_name


@python_2_unicode_compatible 
class Task(models.Model):
    """model of Task"""
    task_name = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    reference = models.CharField(max_length=20)

    def str(self):
        """decorator need method str"""
        return self.task_name

    def __str__(self):
        return self.task_name
   