# Generated by Django 5.1.2 on 2024-10-11 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_request', '0004_servicerequestmodel_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequestmodel',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='requests/'),
        ),
    ]
