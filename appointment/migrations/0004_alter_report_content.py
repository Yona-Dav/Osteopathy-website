# Generated by Django 3.2.10 on 2021-12-22 12:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_auto_20211220_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
