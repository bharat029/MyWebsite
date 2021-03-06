# Generated by Django 2.1.5 on 2019-02-25 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_aboutme'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('definition', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('definition', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbies', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='PossitionsOfResponsibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('definition', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ProfesstionalIntrests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professional_inrests', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('definition', models.CharField(max_length=1000)),
            ],
        ),
    ]
