# Generated by Django 4.0 on 2022-09-18 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprises', '0006_alter_banking_id_alter_businessunit_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banking',
            old_name='bank_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='banking',
            old_name='bank_type',
            new_name='type',
        ),
        migrations.AddField(
            model_name='banking',
            name='account',
            field=models.CharField(default='000', max_length=255),
        ),
        migrations.AddField(
            model_name='paymentmodes',
            name='account',
            field=models.CharField(default='Ngata_01', max_length=255),
        ),
        migrations.AddField(
            model_name='paymentmodes',
            name='name',
            field=models.CharField(default='Petty Cash', max_length=255),
        ),
        migrations.AddField(
            model_name='paymentmodes',
            name='type',
            field=models.CharField(default='Petty Cash', max_length=255),
        ),
    ]