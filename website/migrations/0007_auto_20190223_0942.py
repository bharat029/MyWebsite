# Generated by Django 2.1.7 on 2019-02-23 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_delete_aboutme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='certificate_link',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
