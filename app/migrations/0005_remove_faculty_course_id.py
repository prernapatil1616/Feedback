# Generated by Django 4.2.5 on 2023-09-17 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_faculty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='course_id',
        ),
    ]
