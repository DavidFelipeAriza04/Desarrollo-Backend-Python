# Generated by Django 5.0.3 on 2024-04-02 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('init_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
    ]
