# Generated by Django 3.2.18 on 2023-04-24 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skilltest', '0004_alter_testsessionitems_user_video_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsessionitems',
            name='session_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='skilltest.testsessioninfo'),
        ),
    ]