# Generated by Django 3.1.3 on 2020-12-19 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20201219_1458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='total_ques',
            new_name='total_questions',
        ),
    ]