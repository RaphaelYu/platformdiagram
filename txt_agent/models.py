# -*- coding: utf-8 -*-
"""agent model which both on client and worker"""
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Agent(models.Model):
    """model of agent """
    agent_id = models.CharField(max_length=32)

    def str(self):
        """decorate required """
        return self.agent_id

    def __str__(self):
        return self.agent_id

@python_2_unicode_compatible
class Action(models.Model):
    """model actions  as a worker """
    action_name = models.CharField(max_length=32)

    def str(self):
        """decorator required"""
        return self.action_name

    def __str__(self):
        return self.action_name
    