# Generated by Django 2.0.8 on 2018-12-05 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='size',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]