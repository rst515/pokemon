# Generated by Django 3.2.15 on 2022-09-25 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0008_delete_pokemonapi'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pokemon',
            options={'ordering': ['pokemon_id']},
        ),
    ]
