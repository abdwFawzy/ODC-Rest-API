# Generated by Django 3.2.15 on 2022-10-06 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20221006_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(through='api.EnrolledIn', to='api.Student'),
        ),
    ]
