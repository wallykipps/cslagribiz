# Generated by Django 4.0 on 2022-08-10 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0028_rename_package_feedtypes_unitmeasure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='unit',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='layers.feedtypes', verbose_name='unit'),
        ),
    ]