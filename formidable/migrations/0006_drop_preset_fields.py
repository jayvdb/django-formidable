from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formidable', '0005_conditions_default'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preset',
            name='form',
        ),
        migrations.RemoveField(
            model_name='presetarg',
            name='preset',
        ),
    ]
