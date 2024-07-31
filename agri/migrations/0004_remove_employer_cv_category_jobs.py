# Generated by Django 4.2.13 on 2024-07-30 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0003_employer_cv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='cv',
        ),
        migrations.AddField(
            model_name='category',
            name='jobs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='agri.joblisting'),
        ),
    ]
