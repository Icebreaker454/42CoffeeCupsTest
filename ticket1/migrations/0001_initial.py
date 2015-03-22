# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('birth_date', models.DateField()),
                ('bio', models.TextField()),
                ('contacts_email', models.EmailField(max_length=128)),
                ('contacts_jabber_id', models.EmailField(max_length=75)),
                ('contacts_skype_id', models.CharField(max_length=32)),
                ('contacts_other', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
