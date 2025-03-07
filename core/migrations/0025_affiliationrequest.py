# Generated by Django 5.1.6 on 2025-03-04 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_hospital_affiliated_hospitals'),
    ]

    operations = [
        migrations.CreateModel(
            name='AffiliationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('from_hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_requests', to='core.hospital')),
                ('to_hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_requests', to='core.hospital')),
            ],
        ),
    ]
