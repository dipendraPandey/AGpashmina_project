# Generated by Django 3.1.1 on 2020-09-26 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutcompany',
            options={'verbose_name': 'Company Detail', 'verbose_name_plural': 'Company Details'},
        ),
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contact Info'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Team Member', 'verbose_name_plural': 'Company Team'},
        ),
    ]
