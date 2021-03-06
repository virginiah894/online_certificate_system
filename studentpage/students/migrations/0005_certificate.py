# Generated by Django 3.2.5 on 2021-07-15 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.course')),
                ('grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.grade')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
    ]
