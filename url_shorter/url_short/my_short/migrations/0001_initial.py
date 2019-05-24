# Generated by Django 2.2.1 on 2019-05-23 19:17

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
            name='UrlTable',
            fields=[
                ('long_url', models.TextField(max_length=400)),
                ('key_url', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('data_filed', models.DateField(auto_now_add=True)),
                ('click', models.IntegerField(default=0)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]