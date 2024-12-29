# Generated by Django 5.1.4 on 2024-12-29 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('card', 'Card'), ('cash', 'Cash'), ('savings', 'Savings'), ('investment', 'Investment')], max_length=100)),
            ],
            options={
                'db_table': 'account_type',
            },
        ),
        migrations.CreateModel(
            name='AmountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('fixed_expense', 'Fixed Expense'), ('variable_expense', 'Variable Expense'), ('fixed_income', 'Fixed Income'), ('variable_income', 'Variable Income')], max_length=100)),
            ],
            options={
                'db_table': 'amount_type',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=100)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.accounttype')),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.accounts')),
                ('amount_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.amounttype')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.categories')),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
    ]
