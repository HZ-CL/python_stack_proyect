# Generated by Django 3.1.6 on 2021-02-24 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='Desc',
            field=models.CharField(default='dojo antiguo', max_length=255),
            preserve_default=False,
        ),
    ]
