# Generated by Django 3.2.18 on 2023-04-24 05:56

from django.db import migrations, models
import skilltest.utils


class Migration(migrations.Migration):

    dependencies = [
        ('skilltest', '0005_alter_testsessionitems_session_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsessionitems',
            name='user_video_path',
            field=models.FileField(upload_to=skilltest.utils.user_directory_path),
        ),
    ]
