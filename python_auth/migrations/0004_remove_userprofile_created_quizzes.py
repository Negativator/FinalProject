# Generated by Django 3.1.3 on 2020-12-18 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('python_auth', '0003_userprofile_created_quizzes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='created_quizzes',
        ),
    ]
