# Generated by Django 3.1.7 on 2021-04-19 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance_System_App', '0002_auto_20210330_0234'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_exam_marks', models.FloatField(default=0)),
                ('subject_assignment_marks', models.FloatField(default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance_System_App.students')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance_System_App.subjects')),
            ],
        ),
    ]
