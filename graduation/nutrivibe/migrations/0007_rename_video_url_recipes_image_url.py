# Generated by Django 4.2.11 on 2024-05-03 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutrivibe', '0006_rename_difficulty_exercises_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipes',
            old_name='video_url',
            new_name='image_url',
        ),
    ]
