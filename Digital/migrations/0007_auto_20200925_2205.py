# Generated by Django 3.0.8 on 2020-09-25 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Digital', '0006_delete_altele'),
    ]

    operations = [
        migrations.AddField(
            model_name='bauturi',
            name='poza',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='desert',
            name='poza',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='principal',
            name='poza',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
