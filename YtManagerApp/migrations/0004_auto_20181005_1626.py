# Generated by Django 2.1.2 on 2018-10-05 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YtManagerApp', '0003_auto_20181003_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='downloaded_path',
            field=models.TextField(blank=True, null=True),
        ),
    ]