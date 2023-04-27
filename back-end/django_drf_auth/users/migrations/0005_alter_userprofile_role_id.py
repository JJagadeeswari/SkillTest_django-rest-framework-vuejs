# Generated by Django 3.2.18 on 2023-04-24 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofile_role_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='users.role'),
        ),
    ]
