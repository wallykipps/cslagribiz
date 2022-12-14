# Generated by Django 4.0 on 2022-09-18 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enterprises', '0007_rename_bank_name_banking_name_and_more'),
        ('layers', '0046_alter_batch_options_alter_birdsstock_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashbalance',
            name='banking',
        ),
        migrations.AddField(
            model_name='cashbalance',
            name='credit_ac',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credit_ac', to='enterprises.banking', verbose_name='credit_ac'),
        ),
        migrations.AddField(
            model_name='cashbalance',
            name='debit_ac',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='debit_ac', to='enterprises.banking', verbose_name='debit_ac'),
        ),
    ]
