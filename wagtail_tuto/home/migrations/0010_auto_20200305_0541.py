# Generated by Django 2.0 on 2020-03-05 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200305_0538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='copywritingsettings',
            old_name='testimonial',
            new_name='event',
        ),
    ]