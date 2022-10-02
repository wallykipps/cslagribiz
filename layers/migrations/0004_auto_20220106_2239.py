# Generated by Django 3.1.2 on 2022-01-06 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enterprises', '0002_auto_20220106_1137'),
        ('layers', '0003_auto_20220106_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='batch',
            name='createdBy',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='createdBy'),
        ),
        migrations.AddField(
            model_name='birdsstock',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='creditexpenses',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='creditsales',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='expenses',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='production',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='EggsInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_date', models.DateField()),
                ('egg_loss_defects', models.IntegerField(blank=True, null=True)),
                ('egg_loss_breakages', models.IntegerField(blank=True, null=True)),
                ('egg_loss_unaccounted', models.IntegerField(blank=True, null=True)),
                ('eggs_stock_actual_crates', models.IntegerField(blank=True, null=True)),
                ('eggs_stock_actual_pieces', models.IntegerField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layers.batch', verbose_name='batch')),
                ('businessunit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprises.businessunit', verbose_name='businessunit')),
                ('enterprisetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprises.enterprisetype', verbose_name='enterprisetype')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprises.staff', verbose_name='staff')),
            ],
            options={
                'verbose_name_plural': 'Eggs Inventory',
                'ordering': ['inventory_date'],
            },
        ),
    ]
