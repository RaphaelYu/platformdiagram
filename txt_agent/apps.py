# -*- coding: utf-8 -*-
"""zero mq django application """
from __future__ import unicode_literals

from django.apps import AppConfig
from zmq import Context

class TxtAgentConfig(AppConfig):
    """agent config """
    name = 'txt_agent'


class Agent(object):
    """Agent class on the zmq context"""
    def __init__(self):
        self.ctxt = Context.instance()
