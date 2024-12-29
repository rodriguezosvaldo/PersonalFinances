from rest_framework import serializers
from .models import AccountType, AmountType, Accounts, Categories, Transactions

def create_serializer(model_name):
    class Serializer(serializers.ModelSerializer):
        class Meta:
            model = model_name
            fields = '__all__'
    return Serializer

AccountTypeSerializer = create_serializer(AccountType)
AmountTypeSerializer = create_serializer(AmountType)
AccountsSerializer = create_serializer(Accounts)
CategoriesSerializer = create_serializer(Categories)
TransactionsSerializer = create_serializer(Transactions)


    


