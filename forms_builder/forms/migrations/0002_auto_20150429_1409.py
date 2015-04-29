# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='field_type',
            field=models.IntegerField(verbose_name='Type', choices=[(1, 'Single line text'), (2, 'Multi line text'), (3, 'Email'), (13, 'Number'), (14, 'URL'), (4, 'Check box'), (5, 'Check boxes'), (6, 'Drop down'), (7, 'Multi select'), (8, 'Radio buttons'), (9, 'File upload'), (10, 'Date'), (11, 'Date/time'), (15, 'Date of birth'), (12, 'Hidden'), (103, 'Desktop Geometry Field'), (107, 'ReCaptchaField')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='form',
            name='sites',
            field=models.ManyToManyField(default=[1], related_name='forms_form_forms', editable=False, to='sites.Site'),
            preserve_default=True,
        ),
    ]
