# network_manager/forms.py
from django import forms
from .models import Contract
from .models import DedicatedProvider
from .models import ExternalIP
from .models import MikrotikGW
from .models import MobileProvider
from .models import NetworkDevice
from .models import Service


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['provider', 'contract_number', 'contact_person', 'email']



class DedicatedProviderForm(forms.ModelForm):
    class Meta:
        model = DedicatedProvider
        fields = ['service_type', 'connection_type', 'speed', 'gateway']
        widgets = {
            'service_type': forms.Select(),
            'connection_type': forms.Select(),
            'speed': forms.Select(),
            'gateway': forms.Select(),  # Предполагается, что gateway - это ForeignKey
        }



class ExternalIPForm(forms.ModelForm):
    class Meta:
        model = ExternalIP
        fields = ['dedicated_provider', 'ip_address', 'mask', 'gw']
        widgets = {
            'dedicated_provider': forms.Select(),  # Предполагается, что это ForeignKey
            'ip_address': forms.TextInput(),
            'mask': forms.TextInput(),
            'gw': forms.TextInput(),
        }



class MikrotikGWForm(forms.ModelForm):
    class Meta:
        model = MikrotikGW
        fields = ['name', 'description', 'site', 'ip_address', 'login', 'password',
                  'loopback_ip', 'ext_ip', 'ext_gw', 'gre1', 'gre2', 'gre3', 'gre4']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите название'}),
            'description': forms.Textarea(attrs={'placeholder': 'Введите описание'}),
            'site': forms.Select(),  # Предполагается, что это ForeignKey
            'ip_address': forms.TextInput(attrs={'placeholder': 'Введите IP-адрес'}),
            'login': forms.TextInput(attrs={'placeholder': 'Введите логин'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}),
            'loopback_ip': forms.TextInput(attrs={'placeholder': 'Введите IP адрес Loopback'}),
            'ext_ip': forms.TextInput(attrs={'placeholder': 'Введите внешний IP адрес'}),
            'ext_gw': forms.TextInput(attrs={'placeholder': 'Введите внешний шлюз'}),
            'gre1': forms.TextInput(attrs={'placeholder': 'Введите GRE1'}),
            'gre2': forms.TextInput(attrs={'placeholder': 'Введите GRE2'}),
            'gre3': forms.TextInput(attrs={'placeholder': 'Введите GRE3'}),
            'gre4': forms.TextInput(attrs={'placeholder': 'Введите GRE4'}),
        }

class MobileProviderForm(forms.ModelForm):
    class Meta:
        model = MobileProvider
        fields = ['operator', 'sim_card_number']
        widgets = {
            'operator': forms.TextInput(attrs={'placeholder': 'Введите оператора'}),
            'sim_card_number': forms.TextInput(attrs={'placeholder': 'Введите номер SIM-карты'}),
        }


class NetworkDeviceForm(forms.ModelForm):
    class Meta:
        model = NetworkDevice
        fields = ['name', 'description', 'site', 'ip_address', 'login', 'password']
        widgets = {
            'password': forms.PasswordInput(),  # Скрыть ввод пароля
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_type', 'connection_type', 'speed']  # Укажите поля, которые хотите включить в форму

# forms.py
from django import forms
from .models import Site

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'description', 'address', 'td', 'legal_entity',
                  'data_subnet', 'voice_subnet', 'tech_subnet', 'iot_subnet']
