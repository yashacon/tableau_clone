# Generated by Django 3.1.6 on 2021-02-17 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210217_1831'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='session_start',
            new_name='Transaction',
        ),
    ]
