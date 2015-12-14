# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150527_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='标题',
            new_name='title',
        ),
    ]
