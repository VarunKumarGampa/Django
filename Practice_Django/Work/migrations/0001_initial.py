# Generated by Django 5.1.1 on 2024-10-06 21:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Github_url', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='profile_pics/')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('AWS', 'AWS Practice'), ('nodejs', 'tour-app')], max_length=10)),
            ],
        ),
    ]
