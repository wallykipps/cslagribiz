# Generated by Django 4.0 on 2022-06-01 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0017_alter_production_birds'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='name',
            new_name='customer_name',
        ),
    ]
