# Generated by Django 3.1.1 on 2021-07-06 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_1', models.SmallIntegerField(verbose_name='Start Year')),
                ('year_2', models.SmallIntegerField(verbose_name='End Year')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
            ],
            options={
                'verbose_name': 'Session',
                'verbose_name_plural': 'Sessions',
                'db_table': 'events_tranport_sessions',
                'ordering': ['year_1'],
                'managed': True,
                'unique_together': {('year_1', 'year_2')},
            },
        ),
        migrations.CreateModel(
            name='TransportEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.PositiveIntegerField(choices=[(1, 'Alpha'), (2, 'Omega')], verbose_name='Semester')),
                ('start_date', models.DateTimeField(verbose_name='Registration Start Date')),
                ('end_date', models.DateTimeField(verbose_name='Registration End Date')),
                ('payment_start_date', models.DateTimeField(verbose_name='Payment Start Date')),
                ('payment_end_date', models.DateTimeField(verbose_name='Payment Start Date')),
                ('transport_date', models.DateField(verbose_name='Transport Date')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('payment_active', models.BooleanField(default=False, verbose_name='Payment Active')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Timestamp')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.session', verbose_name='Session')),
            ],
            options={
                'verbose_name': 'Transport Event',
                'verbose_name_plural': 'Transport Events',
                'db_table': 'events_transport',
                'managed': True,
                'unique_together': {('session', 'semester', 'start_date', 'end_date', 'payment_start_date', 'payment_end_date', 'transport_date')},
            },
        ),
        migrations.CreateModel(
            name='TradeFairEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.PositiveIntegerField(choices=[(1, 'Alpha'), (2, 'Omega')], verbose_name='Semester')),
                ('theme', models.CharField(max_length=50, verbose_name='Event Theme')),
                ('start_date', models.DateTimeField(verbose_name='Booking Start Date')),
                ('end_date', models.DateTimeField(verbose_name='Booking End Date')),
                ('fair_start_date', models.DateTimeField(verbose_name='Trade Fair Start Date')),
                ('fair_end_date', models.DateTimeField(verbose_name='Trade Fair End Date')),
                ('fair_note', models.TextField(verbose_name='Note on Trade Fair procedure')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.session', verbose_name='Session')),
            ],
            options={
                'verbose_name': 'Trade Fair Event',
                'verbose_name_plural': 'Trade Fair Events',
                'db_table': 'events_trade_fair',
                'managed': True,
                'unique_together': {('session', 'semester', 'theme', 'start_date', 'end_date', 'fair_start_date', 'fair_end_date')},
            },
        ),
        migrations.CreateModel(
            name='LuggageEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.PositiveIntegerField(choices=[(1, 'Alpha'), (2, 'Omega')], verbose_name='Semester')),
                ('start_date', models.DateTimeField(verbose_name='Registration Start Date')),
                ('end_date', models.DateTimeField(verbose_name='Registraion End Date')),
                ('deposit_start_date', models.DateTimeField(verbose_name='Deposit Start Date')),
                ('deposit_end_date', models.DateTimeField(verbose_name='Deposit End Date')),
                ('deposit_note', models.TextField(blank=True, null=True, verbose_name='Note on Deposit procedure')),
                ('deposit_active', models.BooleanField(default=False, verbose_name='Deposite Status')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.session', verbose_name='Session')),
            ],
            options={
                'verbose_name': 'Luggage Event',
                'verbose_name_plural': 'Luggage Events',
                'db_table': 'events_luggage',
                'managed': True,
                'unique_together': {('session', 'semester', 'start_date', 'end_date', 'deposit_start_date', 'deposit_end_date')},
            },
        ),
    ]