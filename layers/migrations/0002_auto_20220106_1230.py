# Generated by Django 3.1.2 on 2022-01-06 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batch',
            options={'ordering': ['-delivery_date'], 'verbose_name_plural': 'Batches'},
        ),
        migrations.AlterModelOptions(
            name='birdsstock',
            options={'ordering': ['-batch'], 'verbose_name_plural': 'Birds Stock'},
        ),
        migrations.AlterField(
            model_name='birdsstock',
            name='birds_stock_actual',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='birdsstock',
            name='stock_movement_notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
