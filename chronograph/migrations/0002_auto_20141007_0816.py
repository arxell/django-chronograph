# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chronograph', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='args',
            field=models.TextField(help_text='Space separated list; e.g: arg1 option1=True', verbose_name='args', blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='shell_command',
            field=models.TextField(verbose_name='shell command', blank=True),
        ),
    ]
