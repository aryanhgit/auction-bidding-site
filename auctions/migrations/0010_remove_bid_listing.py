# Generated by Django 5.1.7 on 2025-04-01 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_remove_bid_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='listing',
        ),
    ]
