# network_manager/forms.py
from django import forms
from .models import Contract

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['provider', 'contract_number', 'contact_person', 'email']
