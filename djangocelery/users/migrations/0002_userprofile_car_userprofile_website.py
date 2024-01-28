# Generated by Django 4.2.9 on 2024-01-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='car',
            field=models.CharField(choices=[('mazda', 'Mazda Axela'), ('toyota', 'Toyota TX'), ('honda', 'Honda CR-V')], default='mazda', max_length=256),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='website',
            field=models.CharField(max_length=256, null=True),
        ),
    ]