# Generated by Django 3.0.3 on 2020-04-22 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AIRecruiterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.CharField(max_length=1000)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.AIRecruiterUser')),
            ],
            options={
                'db_table': 'resume',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100, null=True)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.AIRecruiterUser')),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]
