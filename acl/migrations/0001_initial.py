# Generated by Django 2.1.4 on 2018-12-07 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hadInstructionFor', to='members.Member')),
                ('issuer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='isInstructedBy', to='members.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('requires_instruction', models.BooleanField(default=False)),
                ('requires_form', models.BooleanField(default=False)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='is_located', to='acl.Location')),
                ('requires_permit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='has_permit', to='members.PermitType')),
            ],
        ),
        migrations.AddField(
            model_name='instruction',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acl.Machine'),
        ),
    ]
