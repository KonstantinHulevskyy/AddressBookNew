# Generated by Django 3.1.2 on 2021-11-08 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addressbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
