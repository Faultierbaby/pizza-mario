# Generated by Django 3.1.2 on 2021-01-14 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestellung', '0012_auto_20210114_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='zutatnummer',
        ),
        migrations.AddField(
            model_name='pizza',
            name='zutatnummer',
            field=models.ManyToManyField(to='bestellung.Zutat'),
        ),
    ]