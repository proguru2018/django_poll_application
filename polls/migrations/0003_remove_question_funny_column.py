# Generated by Django 3.1.3 on 2021-09-12 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_funny_column'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='funny_column',
        ),
    ]
