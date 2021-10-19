# Generated by Django 3.2.6 on 2021-10-19 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('write', '0003_shortnote_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortnote',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shortnote',
            name='status',
            field=models.CharField(choices=[('important', 'important'), ('warning', 'warning'), ('note', 'note')], default='', max_length=1000),
        ),
    ]
