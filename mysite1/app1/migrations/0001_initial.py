# Generated by Django 4.1.7 on 2023-03-02 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100, null=True)),
                ('lname', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=255, null=True, unique=True)),
                ('current_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
