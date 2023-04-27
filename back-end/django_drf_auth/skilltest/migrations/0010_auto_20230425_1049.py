# Generated by Django 3.2.18 on 2023-04-25 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skilltest', '0009_auto_20230424_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='testsessionitems',
            name='comments',
            field=models.TextField(blank=True, default='None'),
        ),
        migrations.AddField(
            model_name='testsessionitems',
            name='rating',
            field=models.CharField(choices=[('Null', '0'), ('Bad', '1'), ('Need_to_Improve', '2'), ('Average', '3'), ('Good', '4'), ('Excelent', '5')], default=0, max_length=25),
        ),
    ]
