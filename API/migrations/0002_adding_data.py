from django.db import migrations

def adding_data(apps, schema_editor):
    AmountType = apps.get_model('API', 'AmountType')
    data_amount_type = [
        {'type':'Fixed Expense'},
        {'type':'Variable Expense'},
        {'type':'Fixed Income'},
        {'type':'Variable Income'}
    ]
    for i in data_amount_type:
        AmountType.objects.create(**i)

    AccountType = apps.get_model('API', 'AccountType')
    data_account_type = [
        {'type':'Card'},
        {'type':'Cash'},
        {'type':'Savings'},
        {'type':'Investment'}
    ]
    for i in data_account_type:
        AccountType.objects.create(**i)

class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial')
    ]

    operations = [
        migrations.RunPython(adding_data)
    ]