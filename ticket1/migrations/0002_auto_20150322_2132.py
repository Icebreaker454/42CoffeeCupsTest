# -*- coding: utf-8 -*-
"""
    This is the migration that loads initial data from a fixture,
    since from Django==1.7 fixture auto loading after each migration
    was deprecated
"""
from __future__ import unicode_literals

import os
from sys import path



from django.db import models
from django.db import migrations
from django.core import serializers
from django.contrib.auth.models import User

FIXTURE_DIRNAME = os.path.abspath(os.path.join(os.path.dirname(__file__), '../', 'fixtures'))
FIXTURE_FILENAME = 'my_data.json'


def load_fixture(apps, schema_editor):
    """ Function that loads data from fixtures """
    fixture_file = os.path.join(FIXTURE_DIRNAME, FIXTURE_FILENAME)
    fixture = open(fixture_file, 'rb')

    objects = serializers.deserialize('json', fixture, ignorenonexistent=True)
    for obj in objects:
        obj.save()
    fixture.close()

def unload_fixture(apps, schema_editor):
    """ Deleting all entries for given models """

    MyModel = apps.get_model('ticket1', 'Person')
    MyModel.objects.all().delete()
    User.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('ticket1', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture)
    ]
