# Generated by Django 3.1.2 on 2022-01-15 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0006_cashbalance_products_stockmovement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='birdsstock',
            name='businessunit',
        ),
        migrations.RemoveField(
            model_name='birdsstock',
            name='enterprisetype',
        ),
    ]
