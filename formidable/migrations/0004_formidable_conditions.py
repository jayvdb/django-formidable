# Generated by Django 1.9.12 on 2017-06-14 12:24

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('formidable', '0003_item_label_no_size_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='formidable',
            name='conditions',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
