# Generated by Django 3.2.18 on 2023-04-24 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userprofile_interest'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role_id',
            field=models.IntegerField(default=2),
        ),
    ]