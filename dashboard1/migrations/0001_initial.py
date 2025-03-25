# Generated by Django 3.1.12 on 2025-03-20 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('end_year', models.CharField(blank=True, max_length=10, null=True)),
                ('intensity', models.IntegerField()),
                ('sector', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('insight', models.TextField()),
                ('url', models.URLField()),
                ('region', models.CharField(max_length=100)),
                ('start_year', models.CharField(blank=True, max_length=10, null=True)),
                ('impact', models.CharField(blank=True, max_length=100, null=True)),
                ('added', models.DateTimeField()),
                ('published', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(max_length=100)),
                ('relevance', models.IntegerField()),
                ('pestle', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('likelihood', models.IntegerField()),
            ],
        ),
    ]
