# Generated by Django 4.1.3 on 2024-06-15 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0006_post_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.CharField(default='', max_length=200),
        ),
    ]