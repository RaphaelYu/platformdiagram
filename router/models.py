# -*- coding: utf-8 -*-
"""model of routers """
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Services(models.Model):
    """model of types of Service """
    service_name = models.CharField(max_length=64)
    amount = models.DecimalField(0)

    def str(self):
        """compatible with python 2.0 give service Name"""
        return self.service_name

    def __str__(self):
        return self.service_name


@python_2_unicode_compatible
class ServiceInstances(models.Model):
    """model of service nodes which observable"""
    service_id = models.CharField(max_length=64)
    ip_address = models.CharField(max_length=128)
    port = models.DecimalField(0)
    service_name = models.ForeignKey(to="Service", \
    on_delete=models.CASCADE)


    def str(self):
        """compatible with python 2.0 give the id """
        return self.service_id

    def __str__(self):
        return self.service_id


@python_2_unicode_compatible
class ProxyInstance(models.Model):
    """model of proxies """
    proxy_id = models.CharField(max_length=64)
    ip_address = models.CharField(max_length=128)
    frontend = models.DecimalField(0)
    backend = models.DecimalField(0)

    def str(self):
        """compatible with python 2.0 give prox_id """
        return self.proxy_id

    def __str__(self):
        return self.proxy_id

@python_2_unicode_compatible
class ServiceBindProxy(models.Model):
    """binding of proxies and service"""
    proxy_id = models.ForeignKey("ProxyInstance")
    server_id= models.ForeignKey("ServiceInstances")
