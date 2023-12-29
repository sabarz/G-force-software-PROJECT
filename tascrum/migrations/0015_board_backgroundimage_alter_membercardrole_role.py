# Generated by Django 4.2.6 on 2023-10-27 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tascrum', '0014_card_reminder'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='backgroundimage',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='membercardrole',
            name='role',
            field=models.CharField(default='member', max_length=50),
        ),
    ]
