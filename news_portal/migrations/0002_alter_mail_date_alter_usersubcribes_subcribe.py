# Generated by Django 5.0.3 on 2024-07-06 14:14

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_portal', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 7, 6, 14, 14, 1, 443744)),
        ),
        migrations.AlterField(
            model_name='usersubcribes',
            name='subcribe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
