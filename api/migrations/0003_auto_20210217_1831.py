# Generated by Django 3.1.6 on 2021-02-17 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_userdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='session_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
