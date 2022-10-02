# Generated by Django 4.0 on 2022-07-18 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0021_alter_customers_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='costcategories',
            options={'ordering': ['id'], 'verbose_name_plural': 'Cost Categories'},
        ),
        migrations.AlterModelOptions(
            name='creditsales',
            options={'ordering': ['instalment_date'], 'verbose_name_plural': 'Credit Sales'},
        ),
        migrations.AddField(
            model_name='creditexpenses',
            name='payment_source',
            field=models.ForeignKey(default=27, on_delete=django.db.models.deletion.CASCADE, related_name='payment_from', to='layers.batch', verbose_name='payment_source'),
        ),
    ]
