# Generated by Django 2.0 on 2017-12-12 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20171211_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.FileField(upload_to='images/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]