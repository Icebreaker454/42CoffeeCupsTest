# -*- coding: utf-8 -*-

"""
    The models file for ticket1
"""
from django.db import models


class Person(models.Model):
    """ The Person model itself """

    first_name = models.CharField(
        max_length=128,
        blank=False,
    )
    last_name = models.CharField(
        max_length=128,
        blank=False,
    )
    birth_date = models.DateField(
        blank=False,
    )
    bio = models.TextField()
    contacts_email = models.EmailField(
        max_length=128,
        blank=False
    )
    contacts_jabber_id = models.EmailField()
    contacts_skype_id = models.CharField(
        max_length=32
    )
    contacts_other = models.TextField()