# Generated by Django 3.2.16 on 2022-10-09 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_enrolledin_start_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='admin',
        ),
        migrations.RemoveField(
            model_name='student',
            name='status',
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='', max_length=255, unique=True, verbose_name='email address'),
            preserve_default=False,
        ),
    ]
