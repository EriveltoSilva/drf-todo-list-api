# Generated by Django 5.1 on 2024-08-09 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_priority_alter_todo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('low', 'Baixa'), ('middle', 'Media'), ('high', 'Alta')], default=('low', 'Baixa'), max_length=20),
        ),
    ]
