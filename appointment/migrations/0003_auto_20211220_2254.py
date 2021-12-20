# Generated by Django 3.2.10 on 2021-12-20 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_rename_gender_profile_sex'),
        ('appointment', '0002_alter_schedule_options'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together={('date', 'hour')},
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.schedule')),
            ],
        ),
    ]
