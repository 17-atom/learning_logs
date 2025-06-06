# Generated by Django 5.1.7 on 2025-03-23 22:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logss', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_logss.tema')),
            ],
            options={
                'verbose_name_plural': 'entradas',
            },
        ),
    ]
