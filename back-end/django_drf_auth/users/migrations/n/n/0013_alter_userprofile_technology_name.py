# Generated by Django 4.2 on 2023-05-08 06:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0012_alter_userprofile_technology_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="technology_name",
            field=models.CharField(default="General", max_length=200),
        ),
    ]
