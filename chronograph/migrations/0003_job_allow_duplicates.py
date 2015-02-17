# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chronograph', '0002_auto_20141007_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='allow_duplicates',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
