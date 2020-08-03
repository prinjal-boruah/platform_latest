# Generated by Django 2.1.15 on 2020-05-14 09:13

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
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.BigIntegerField()),
                ('name_on_card', models.CharField(max_length=100)),
                ('expiry_date', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=150)),
                ('comm_address1', models.TextField()),
                ('comm_address2', models.TextField()),
                ('comm_country', models.CharField(max_length=150)),
                ('comm_state', models.CharField(max_length=150)),
                ('comm_city', models.CharField(max_length=150)),
                ('comm_phone', models.BigIntegerField()),
                ('comm_email', models.EmailField(max_length=254)),
                ('comm_gstin', models.CharField(max_length=150)),
                ('bill_address1', models.TextField()),
                ('bill_address2', models.TextField()),
                ('bill_country', models.CharField(max_length=150)),
                ('bill_state', models.CharField(max_length=150)),
                ('bill_city', models.CharField(max_length=150)),
                ('bill_phone', models.BigIntegerField()),
                ('bill_email', models.EmailField(max_length=254)),
                ('bill_gstin', models.CharField(max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('duration', models.IntegerField()),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platform_app.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('number_of_stakeholders', models.IntegerField()),
                ('price', models.BigIntegerField()),
                ('created', models.DateTimeField()),
                ('validity', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='subscribed_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='platform_app.SubscriptionPlan'),
        ),
        migrations.AddField(
            model_name='card',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platform_app.Organization'),
        ),
    ]
