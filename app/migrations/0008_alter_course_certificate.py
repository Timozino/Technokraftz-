# Generated by Django 4.1.2 on 2022-10-26 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_course_certificate_course_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Certificate',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
