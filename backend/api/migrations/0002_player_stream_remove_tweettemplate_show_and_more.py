# Generated by Django 5.1 on 2024-08-17 22:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('nickname', models.CharField(blank=True, max_length=255, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('hometown', models.CharField(blank=True, max_length=255, null=True)),
                ('nationality', models.CharField(blank=True, max_length=255, null=True)),
                ('profession', models.CharField(blank=True, max_length=255, null=True)),
                ('first_session_date', models.DateField(blank=True, null=True)),
                ('total_net_winnings', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('total_episodes', models.IntegerField(default=0)),
                ('total_hours_played', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('avg_table_bb', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('biography', models.TextField(blank=True, null=True)),
                ('social_media_handles', models.JSONField(blank=True, default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tweettemplate',
            name='show',
        ),
        migrations.AddField(
            model_name='tweettemplate',
            name='variables',
            field=models.JSONField(default=dict),
        ),
        migrations.CreateModel(
            name='ScheduledTweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduled_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('sent', 'Sent'), ('failed', 'Failed')], default='pending', max_length=10)),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tweettemplate')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('game_type', models.CharField(max_length=255)),
                ('stakes_played', models.CharField(max_length=255)),
                ('effective_bb', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.stream')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerSessionStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('net_winnings', models.DecimalField(decimal_places=2, max_digits=15)),
                ('vpip', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('pfr', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('hours_played', models.DecimalField(decimal_places=2, max_digits=5)),
                ('hourly', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bb_per_hour', models.DecimalField(decimal_places=2, max_digits=10)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.player')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.session')),
            ],
            options={
                'unique_together': {('player', 'session')},
            },
        ),
    ]
