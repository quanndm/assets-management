# Generated by Django 4.2.7 on 2023-11-19 04:36

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=200)),
                ('gender', models.CharField(blank=True, default='M', max_length=1, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('avatar', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('phone_number', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]