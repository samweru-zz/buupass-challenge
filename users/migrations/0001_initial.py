# Generated by Django 4.0.1 on 2022-01-06 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthSub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subordinate', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='subordinate', to=settings.AUTH_USER_MODEL)),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='supervisor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
