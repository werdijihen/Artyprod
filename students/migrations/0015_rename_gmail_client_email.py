# Generated by Django 4.1.7 on 2023-05-20 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0014_personnel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='email',
            new_name='email',
        ),
    ]
