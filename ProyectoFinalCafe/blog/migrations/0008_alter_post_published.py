# Generated by Django 3.2.7 on 2021-11-09 14:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 14, 56, 32, 650101, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
    ]