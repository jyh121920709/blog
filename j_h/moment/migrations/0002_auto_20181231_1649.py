# Generated by Django 2.1.3 on 2018-12-31 08:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('moment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logpost',
            name='article_tag',
        ),
        migrations.AddField(
            model_name='logpost',
            name='log_tag',
            field=models.ManyToManyField(blank=True, related_name='log_tag', to='moment.LogTag'),
        ),
        migrations.AlterField(
            model_name='logpost',
            name='column',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log_post', to='moment.LogColumn'),
        ),
        migrations.AlterField(
            model_name='logpost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 31, 8, 49, 1, 333099, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='logpost',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='log_like', to=settings.AUTH_USER_MODEL),
        ),
    ]