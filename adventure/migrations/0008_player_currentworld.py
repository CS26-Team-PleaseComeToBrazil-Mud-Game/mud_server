# Generated by Django 3.0.3 on 2020-03-05 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0007_auto_20200305_0541'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='currentWorld',
            field=models.IntegerField(default=0),
        ),
    ]