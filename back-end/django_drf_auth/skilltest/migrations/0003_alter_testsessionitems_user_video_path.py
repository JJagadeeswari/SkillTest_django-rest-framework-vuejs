# Generated by Django 3.2.18 on 2023-04-21 09:41

from django.db import migrations, models
import skilltest.models.test_session


class Migration(migrations.Migration):

    dependencies = [
        ('skilltest', '0002_remove_testsessionitems_question_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsessionitems',
            name='user_video_path',
            field=models.FileField(upload_to=skilltest.models.test_session.user_directory_path),
        ),
    ]