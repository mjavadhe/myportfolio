# Generated by Django 4.2.11 on 2025-03-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_full_description_project_is_featured_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='technologies2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='technologies3',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='technologies4',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
