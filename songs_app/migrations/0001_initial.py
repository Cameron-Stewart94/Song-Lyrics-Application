# Generated by Django 2.1.7 on 2019-04-16 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.CharField(max_length=264)),
                ('lyrics', models.TextField(blank=True, null=True)),
                ('artist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='songs_app.Artist')),
            ],
        ),
    ]
