# Generated by Django 5.2.4 on 2025-07-29 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('Librarian', 'Librarian'), ('Member', 'Member'), ('Admin', 'Admin')], default='member', max_length=50),
        ),
    ]
