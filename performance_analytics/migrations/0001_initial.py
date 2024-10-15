# Generated by Django 5.0.1 on 2024-10-10 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerformanceAnalytics',
            fields=[
                ('analy_id', models.AutoField(primary_key=True, serialize=False)),
                ('average_score', models.FloatField(default=0.0)),
                ('completion_rate', models.FloatField(default=0.0)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'performance_analytics',
            },
        ),
    ]
