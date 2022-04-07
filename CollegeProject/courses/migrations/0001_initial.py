# Generated by Django 4.0.3 on 2022-04-07 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=80)),
                ('course_code', models.CharField(max_length=10)),
                ('course_faculty', models.CharField(max_length=50)),
                ('course_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.teachers')),
            ],
        ),
    ]