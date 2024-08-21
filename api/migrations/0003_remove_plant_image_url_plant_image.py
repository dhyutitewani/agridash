# Generated by Django 5.1 on 2024-08-21 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_plant_body_plant_image_url_plant_management_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='image_url',
        ),
        migrations.AddField(
            model_name='plant',
            name='image',
            field=models.ImageField(null=True, upload_to='plants/'),
        ),
    ]
