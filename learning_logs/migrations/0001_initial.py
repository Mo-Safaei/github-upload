# Generated by Django 3.1.6 on 2021-02-12 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=200)),
                ('singer_name', models.CharField(blank=True, max_length=200, null=True)),
                ('Released', models.CharField(blank=True, max_length=200, null=True)),
                ('Album', models.CharField(blank=True, max_length=200, null=True)),
                ('Songwriter', models.CharField(blank=True, max_length=200, null=True)),
                ('Composer', models.CharField(blank=True, max_length=200, null=True)),
                ('Lyrics', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('singer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='learning_logs.singer')),
            ],
        ),
    ]