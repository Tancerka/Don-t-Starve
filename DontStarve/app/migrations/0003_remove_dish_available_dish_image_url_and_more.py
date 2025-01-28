# Generated by Django 5.1.4 on 2025-01-28 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='available',
        ),
        migrations.AddField(
            model_name='dish',
            name='image_url',
            field=models.URLField(default='https://example.com/placeholder.jpg'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
