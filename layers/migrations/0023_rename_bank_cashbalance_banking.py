# Generated by Django 4.0 on 2022-08-04 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0022_alter_costcategories_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cashbalance',
            old_name='bank',
            new_name='banking',
        ),
    ]
