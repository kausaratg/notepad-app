# Generated by Django 4.0.6 on 2022-07-15 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_app', '0003_alter_note_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='status',
            field=models.IntegerField(choices=[(0, 'not_starred'), (1, 'is_starred')], default=0),
        ),
    ]