# Generated by Django 4.0 on 2022-10-20 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0047_remove_cashbalance_banking_cashbalance_credit_ac_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='birdsstock',
            options={'ordering': ['stock_date'], 'verbose_name_plural': 'Birds Stock'},
        ),
        migrations.AlterModelOptions(
            name='vendors',
            options={'ordering': ['vendor_date'], 'verbose_name_plural': 'Vendors'},
        ),
    ]