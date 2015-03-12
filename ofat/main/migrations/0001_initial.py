# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='email (*)')),
                ('firstname', models.CharField(max_length=200, blank=True, verbose_name='first name', null=True)),
                ('lastname', models.CharField(max_length=200, blank=True, verbose_name='last name', null=True)),
                ('institute', models.CharField(max_length=200, blank=True, verbose_name='forensic institute/lab', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
