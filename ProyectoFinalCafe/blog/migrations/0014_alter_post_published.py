# Generated by Django 3.2.7 on 2021-11-29 21:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 29, 21, 43, 2, 240559, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
    ]
