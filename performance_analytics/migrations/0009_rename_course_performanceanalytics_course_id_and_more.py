# Generated by Django 5.0.1 on 2024-10-15 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('performance_analytics', '0008_alter_performanceanalytics_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='performanceanalytics',
            old_name='course',
            new_name='course_id',
        ),
        migrations.RenameField(
            model_name='performanceanalytics',
            old_name='user',
            new_name='user_id',
        ),
    ]