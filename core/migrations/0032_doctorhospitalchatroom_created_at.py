# Generated by Django 5.1.6 on 2025-03-06 21:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_rename_room_doctorhospitalchatmessage_chat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorhospitalchatroom',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
