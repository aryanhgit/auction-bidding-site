# Generated by Django 5.1.7 on 2025-04-01 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_remove_listing_current_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='updated_at',
        ),
    ]
