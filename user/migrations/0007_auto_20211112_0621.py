# Generated by Django 3.2.9 on 2021-11-12 06:21

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_userdetails_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=user.models.nameFile),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
