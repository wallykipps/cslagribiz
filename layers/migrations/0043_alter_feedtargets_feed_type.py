# Generated by Django 4.0 on 2022-08-25 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0042_feedtargets_week_feedtargets_weeks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedtargets',
            name='feed_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layers.costcategories', verbose_name='feed_type'),
        ),
    ]
