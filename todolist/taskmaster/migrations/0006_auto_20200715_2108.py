# Generated by Django 3.0.8 on 2020-07-15 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmaster', '0005_auto_20200715_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(),
        ),
    ]