# Generated by Django 4.0.6 on 2024-05-29 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0004_musica_letra'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='bio',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]