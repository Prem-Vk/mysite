# Generated by Django 4.2.3 on 2023-07-12 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_test_numb2'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='numb3',
            field=models.IntegerField(default=4),
        ),
    ]
