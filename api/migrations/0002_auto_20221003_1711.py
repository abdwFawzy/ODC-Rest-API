# Generated by Django 3.2.15 on 2022-10-03 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrolledin',
            name='course',
        ),
        migrations.RemoveField(
            model_name='enrolledin',
            name='user',
        ),
        migrations.RemoveField(
            model_name='student',
            name='enrolled_in',
        ),
        migrations.RemoveField(
            model_name='student',
            name='userSkills',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Deliverable',
        ),
        migrations.DeleteModel(
            name='EnrolledIn',
        ),
        migrations.DeleteModel(
            name='PrerequisitCourses',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
