# Generated by Django 4.0 on 2022-03-10 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0011_batch_active_alter_batch_id_alter_birdsstock_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batch',
            old_name='active',
            new_name='status',
        ),
    ]
