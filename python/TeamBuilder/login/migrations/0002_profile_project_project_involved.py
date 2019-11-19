# Generated by Django 2.2.5 on 2019-11-19 19:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_username', models.CharField(max_length=20, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message="1. Cannot start or have  '_' or '.' together, only be used once \n 2. Length must be between 8 to 20 characters. \n 3. Only contains alphanumeric characters, '.' and '_' ", regex='^[a-zA-Z0-9]([._](?![._])|[a-zA-Z0-9]){6,18}[a-zA-Z0-9]$')], verbose_name='Username')),
                ('profile_password', models.CharField(max_length=60, verbose_name='Password')),
                ('profile_firstName', models.CharField(max_length=20, verbose_name='First Name')),
                ('profile_lastName', models.CharField(max_length=20, verbose_name='Last Name')),
                ('profile_Email', models.EmailField(max_length=20, verbose_name='E-mail Address')),
                ('profile_PhoneNo', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone Number')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_Name', models.CharField(max_length=60, verbose_name='Name')),
                ('project_Description', models.TextField(max_length=300, verbose_name='Description')),
                ('project_MaxCapacity', models.PositiveIntegerField(default=10, verbose_name='Maximum Capacity')),
                ('project_SpaceTaken', models.PositiveIntegerField(default=1, verbose_name='Space Taken')),
                ('project_SpaceAvailable', models.PositiveIntegerField(blank=True)),
                ('project_Admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Involved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_involved_accepted', models.BooleanField(default=False)),
                ('project_involved_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Project')),
                ('project_involved_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Profile')),
            ],
            options={
                'unique_together': {('project_involved_username', 'project_involved_id')},
            },
        ),
    ]
