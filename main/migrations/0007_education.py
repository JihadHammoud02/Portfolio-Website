# Generated by Django 4.0.5 on 2022-06-14 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_jihad_email_add'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
            ],
        ),
    ]
