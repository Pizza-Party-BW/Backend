# Generated by Django 3.0.2 on 2020-01-09 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0002_auto_20200108_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.CharField(default='An empty passage.', max_length=500),
        ),
        migrations.AlterField(
            model_name='room',
            name='title',
            field=models.CharField(default='Passage', max_length=50),
        ),
    ]