# Generated by Django 4.0.6 on 2022-07-19 04:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_post_created_at_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 18, 22, 27, 48, 149946)),
        ),
    ]
