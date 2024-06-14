# Generated by Django 4.1.3 on 2024-06-12 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0002_reaction_user_subscription_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rare_user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='rareapi.user'),
        ),
    ]