# Generated by Django 2.0 on 2017-12-13 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_auto_20171213_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='keyword',
        ),
        migrations.AlterField(
            model_name='upload',
            name='pic',
            field=models.FileField(upload_to='keyword/'),
        ),
    ]