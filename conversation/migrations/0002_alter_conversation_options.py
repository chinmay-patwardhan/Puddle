# Generated by Django 4.2.3 on 2023-08-01 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conversation',
            options={'ordering': ('-modified_at',)},
        ),
    ]
