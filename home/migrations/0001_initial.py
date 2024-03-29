# Generated by Django 4.0.3 on 2022-03-09 07:23

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
            name='Custom_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fathername', models.CharField(max_length=100)),
                ('mothername', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='image/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
