# Generated by Django 3.1.4 on 2021-01-07 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0003_auto_20210107_1832'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancies',
            options={'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.AlterModelTable(
            name='vacancies',
            table=None,
        ),
    ]
