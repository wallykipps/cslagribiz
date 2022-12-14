# Generated by Django 4.0 on 2022-08-25 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0040_alter_vaccination_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedTargets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekly_feed_per_bird', models.DecimalField(decimal_places=2, max_digits=10)),
                ('feed_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layers.expenses', verbose_name='feed_type')),
            ],
            options={
                'verbose_name_plural': 'Feed Targets',
            },
        ),
    ]
