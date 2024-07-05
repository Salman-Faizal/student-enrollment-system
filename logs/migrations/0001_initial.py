# Generated by Django 5.0.6 on 2024-07-05 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funnel', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('new_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='new_logs', to='funnel.funnelstatus')),
                ('previous_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='previous_logs', to='funnel.funnelstatus')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='students.student')),
            ],
        ),
    ]
