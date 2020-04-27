# Generated by Django 2.1.15 on 2020-04-26 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disks', '0002_auto_20200426_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='bytes',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='track',
            name='milliseconds',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='track',
            name='unitPrice',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
