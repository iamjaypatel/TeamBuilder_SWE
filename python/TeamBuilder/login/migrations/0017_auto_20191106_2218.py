# Generated by Django 2.2.5 on 2019-11-06 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_auto_20191106_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_involved',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]