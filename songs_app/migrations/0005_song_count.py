# Generated by Django 2.1.7 on 2019-04-26 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs_app', '0004_auto_20190424_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
