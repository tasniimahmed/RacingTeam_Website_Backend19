# Generated by Django 2.1.2 on 2019-03-10 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('AuthenticationSystem', '0002_auto_20190309_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userssignup',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='UsersSignUp',
        ),
    ]