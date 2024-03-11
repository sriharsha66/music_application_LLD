# Generated by Django 5.0.3 on 2024-03-11 20:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymp3', '0003_friendrequest_playlist_userprofile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequest',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_requests', to=settings.AUTH_USER_MODEL),
        ),
    ]