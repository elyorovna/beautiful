# Generated by Django 5.1.3 on 2024-11-20 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maxsulot',
            name='narxi',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
