# Generated by Django 5.2 on 2025-04-08 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='image',
            field=models.ImageField(default='static/images/cello-img.jpg', upload_to='upload/img/audio/'),
        ),
    ]
