# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150602_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='内容',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='发表时间',
            new_name='timestamp',
        ),
    ]
