# Generated by Django 4.0.5 on 2022-06-21 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('populate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='retrievedata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=25)),
                ('lname', models.CharField(max_length=25)),
                ('regDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
