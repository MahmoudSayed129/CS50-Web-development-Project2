# Generated by Django 3.2.7 on 2021-09-20 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210920_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='auction_id',
            field=models.IntegerField(default='0'),
        ),
    ]