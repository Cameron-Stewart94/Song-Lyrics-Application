# Generated by Django 2.1.7 on 2019-04-24 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs_app', '0002_auto_20190424_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs_app.Artist'),
        ),
    ]
