# Generated by Django 3.2.18 on 2023-04-24 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_userprofile_role_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='role_id',
        ),
    ]
