# Generated by Django 3.1.2 on 2022-01-15 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprises', '0002_auto_20220106_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=255)),
                ('bank_type', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Banking',
            },
        ),
        migrations.CreateModel(
            name='PaymentModes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_mode', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Payment Mode',
            },
        ),
    ]