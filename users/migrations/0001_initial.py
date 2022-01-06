from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [('auth', '0001_initial')]

    operations = [
        migrations.CreateModel(
        name='AuthSub',
        fields=[
            (
                'id',
                models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID',
                ),
            ),
            (
                'supervisor',
                models.ForeignKey(
                    on_delete=models.deletion.DO_NOTHING,
                    to='auth.user',
                ),
            ),
            (
                'subordinate',
                models.ForeignKey(
                    on_delete=models.deletion.DO_NOTHING,
                    to='auth.user',
                ),
            ),
        ])
    ]