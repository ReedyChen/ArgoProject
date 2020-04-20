# Generated by Django 2.2 on 2020-04-05 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied', models.BooleanField(default=False)),
                ('subject', models.CharField(max_length=4)),
                ('application_name', models.CharField(default='none', max_length=50)),
                ('conudctor', models.CharField(default='none', max_length=50)),
                ('time_slots', models.CharField(default='[]', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('intro', models.TextField(blank=True, help_text='Enter the introduction of this group of program')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('intro', models.TextField(blank=True, help_text='Enter the introduction of this program')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.ProgramGroup')),
            ],
        ),
    ]