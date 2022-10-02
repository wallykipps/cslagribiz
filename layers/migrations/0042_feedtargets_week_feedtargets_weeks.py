# Generated by Django 4.0 on 2022-08-25 11:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0041_feedtargets'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedtargets',
            name='week',
            field=models.CharField(blank=True, default='1', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='feedtargets',
            name='weeks',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]