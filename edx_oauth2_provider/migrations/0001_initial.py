# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrustedClient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client', models.ForeignKey(to='oauth2.Client', on_delete=models.CASCADE)),
            ],
            options={
                'db_table': 'oauth2_provider_trustedclient',
            },
        ),
    ]
