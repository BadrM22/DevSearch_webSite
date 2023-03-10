# Generated by Django 4.1.5 on 2023-01-05 09:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('demo_link', models.URLField(blank=True, max_length=2000, null=True)),
                ('source_link', models.URLField(blank=True, max_length=2000, null=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
