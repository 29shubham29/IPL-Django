# Generated by Django 2.2.6 on 2019-10-11 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipl', '0015_auto_20191011_1143'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='match',
            unique_together={('season', 'team1', 'team2', 'date')},
        ),
    ]
