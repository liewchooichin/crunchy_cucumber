# Generated by Django 5.0.4 on 2024-07-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='id',
            field=models.SmallAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.SmallAutoField(primary_key=True, serialize=False),
        ),
    ]
