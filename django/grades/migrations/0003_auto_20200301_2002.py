# Generated by Django 3.0.3 on 2020-03-01 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0002_grade_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
