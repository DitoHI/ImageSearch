# Generated by Django 2.0 on 2017-12-12 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_auto_20171213_0559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='upload_date',
        ),
        migrations.AddField(
            model_name='upload',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='upload',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
