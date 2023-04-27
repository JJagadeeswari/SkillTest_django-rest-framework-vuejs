# Generated by Django 3.2.18 on 2023-04-20 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('skilltest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionQuestion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('session_video_path', models.FileField(blank=True, upload_to='videos/TestSessionItems/user_directory_path')),
                ('is_active', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skilltest.questions')),
                ('session_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skilltest.testsessioninfo')),
            ],
            options={
                'db_table': 'SessionQuestion',
            },
        ),
    ]