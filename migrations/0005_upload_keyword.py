# Generated by Django 2.0 on 2017-12-12 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='keyword',
            field=models.CharField(default='Some Words', max_length=100),
        ),
    ]
