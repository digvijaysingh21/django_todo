# Generated by Django 5.1.2 on 2024-11-02 04:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todoo',
            options={'ordering': ['-date'], 'verbose_name': 'To-Do Task', 'verbose_name_plural': 'To-Do Tasks'},
        ),
        migrations.AlterField(
            model_name='todoo',
            name='date',
            field=models.DateTimeField(auto_now_add=True, help_text='Timestamp of when the task was created'),
        ),
        migrations.AlterField(
            model_name='todoo',
            name='srno',
            field=models.AutoField(auto_created=True, help_text='Auto-incremented primary key for each task', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todoo',
            name='status',
            field=models.BooleanField(blank=True, default=False, help_text='Completion status of the task (True for completed)'),
        ),
        migrations.AlterField(
            model_name='todoo',
            name='title',
            field=models.CharField(help_text='Short title or description of the task (max 25 characters)', max_length=25),
        ),
        migrations.AlterField(
            model_name='todoo',
            name='user',
            field=models.ForeignKey(help_text='User associated with this task', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]