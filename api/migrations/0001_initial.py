# Generated by Django 3.2.15 on 2022-10-03 04:39

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Deliverable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EnrolledIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, default=datetime.date(2022, 10, 3))),
                ('end_date', models.DateField()),
                ('attendace', models.FloatField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('student_rate', models.FloatField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course')),
            ],
        ),
        migrations.CreateModel(
            name='PrerequisitCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('experience', models.IntegerField(blank=True, null=True)),
                ('enrolled_in', models.ManyToManyField(through='api.EnrolledIn', to='api.Course')),
                ('userSkills', models.ManyToManyField(related_name='students', to='api.Skill')),
            ],
        ),
        migrations.AddField(
            model_name='enrolledin',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_skills',
            field=models.ManyToManyField(related_name='courses', to='api.Skill'),
        ),
        migrations.AddField(
            model_name='course',
            name='deliverables',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='api.deliverable'),
        ),
        migrations.AddField(
            model_name='course',
            name='prerequisit_courses',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='api.prerequisitcourses'),
        ),
        migrations.AddField(
            model_name='course',
            name='prerequisit_skills',
            field=models.ManyToManyField(related_name='pre_courses', to='api.Skill'),
        ),
    ]
