# Generated by Django 4.0 on 2022-06-05 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0019_alter_customers_customer_name_alter_customers_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='product',
            new_name='productname',
        ),
    ]
