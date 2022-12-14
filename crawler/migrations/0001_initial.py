# Generated by Django 3.2.15 on 2022-09-20 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('height', models.IntegerField()),
                ('abilities', models.CharField(max_length=100)),
                ('moves', models.IntegerField()),
                ('official_artwork', models.CharField(blank=True, max_length=50, null=True)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_timestamp', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonAPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_count', models.IntegerField()),
                ('updated_timestamp', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
