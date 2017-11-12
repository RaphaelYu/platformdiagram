# -*- coding: utf-8 -*-
"""application for data agent and proxy in system"""
from __future__ import unicode_literals

from django.apps import AppConfig

import zmq


__zmqContext__ = zmq.Context()
__proxies__ = []


def init_router(proxies):
    """Init routers for application"""
    for proxy in proxies:
        __proxies__.append((proxy.cb,__zmqContext__.socket("REP")))




class RouterConfig(AppConfig):
    name = 'router'
    