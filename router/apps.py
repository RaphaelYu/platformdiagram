# -*- coding: utf-8 -*-
"""application for data agent and proxy in system"""
from __future__ import unicode_literals

from django.apps import AppConfig

import zmq

__agents__ = None

class DataAgent(object):
    """data agent is to collect data and publish data out"""
    def __init__(self):
        self.adddr = None
        self.sock = None
        
class RouterConfig(AppConfig):
    name = 'router'
    