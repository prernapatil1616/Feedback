# Generated by Django 4.2.5 on 2023-09-30 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_feedbackoption'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Average', 'Average'), ('Poor', 'Poor')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.DeleteModel(
            name='FeedbackOption',
        ),
        migrations.AddField(
            model_name='feedbackanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.feedbackquestion'),
        ),
    ]