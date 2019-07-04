# Generated by Django 2.2.1 on 2019-06-10 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skill_management', '0002_skillgroup_skilllevel'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeSkillList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skill_management.Employee')),
            ],
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skill_management.SkillGroup'),
        ),
        migrations.DeleteModel(
            name='SkillList',
        ),
        migrations.AddField(
            model_name='employeeskilllist',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skill_management.Skill'),
        ),
        migrations.AddField(
            model_name='employeeskilllist',
            name='skill_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skill_management.SkillLevel'),
        ),
    ]
