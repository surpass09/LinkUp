# Generated by Django 5.1.6 on 2025-02-19 00:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otlk_micro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='otlk_micro.outlookuserdata'),
        ),
    ]
