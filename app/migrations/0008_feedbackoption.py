# Generated by Django 4.2.5 on 2023-09-30 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
