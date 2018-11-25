# Generated by Django 2.1.3 on 2018-11-19 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactBook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.ForeignKey(null=True, on_delete=models.SET(None), related_name='member_email', to='ContactBook.MemberEmail'),
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.ForeignKey(null=True, on_delete=models.SET(None), related_name='member_phone', to='ContactBook.MemberPhone'),
        ),
    ]