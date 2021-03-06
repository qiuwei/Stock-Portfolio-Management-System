# Generated by Django 2.1.5 on 2019-02-02 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_article_toprecommended'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='description',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='messaging',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='github',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='jobDescription_1',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='jobDescription_2',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='jobDescription_3',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='linkedin',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='wechat_QR_code',
            field=models.URLField(null=True),
        ),
    ]
