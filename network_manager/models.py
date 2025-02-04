
from django.db import models
from django.core.validators import validate_ipv4_address
from ipware import get_client_ip

class Site(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name="Адрес")
    td = models.CharField(max_length=255, verbose_name="Торговая дирекция, регион")
    legal_entity = models.CharField(max_length=255, verbose_name="Юридическое лицо")
    data_subnet = models.GenericIPAddressField(protocol='IPv4', verbose_name="Подсеть Data", blank=True, null=True)
    voice_subnet = models.GenericIPAddressField(protocol='IPv4', verbose_name="Подсеть Voice", blank=True, null=True)
    tech_subnet = models.GenericIPAddressField(protocol='IPv4', verbose_name="Подсеть Tech", blank=True, null=True)
    iot_subnet = models.GenericIPAddressField(protocol='IPv4', verbose_name="Подсеть IoT", blank=True, null=True)

    def __str__(self):
        return self.name

class NetworkDevice(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, verbose_name="Расположение")
    ip_address = models.GenericIPAddressField(protocol='IPv4', verbose_name="IP Адрес")
    login = models.CharField(max_length=255, verbose_name="Логин")
    password = models.CharField(max_length=255, verbose_name="Пароль")

    def __str__(self):
        return self.name

class MikrotikGW(NetworkDevice):
    loopback_ip = models.GenericIPAddressField(protocol='IPv4', verbose_name="IP адрес Loopback")
    ext_ip = models.GenericIPAddressField(protocol='IPv4', verbose_name="Внешний IP адрес")
    ext_gw = models.GenericIPAddressField(protocol='IPv4', verbose_name="Внешний GW")
    gre1 = models.GenericIPAddressField(protocol='IPv4', verbose_name="GRE1", blank=True, null=True)
    gre2 = models.GenericIPAddressField(protocol='IPv4', verbose_name="GRE2", blank=True, null=True)
    gre3 = models.GenericIPAddressField(protocol='IPv4', verbose_name="GRE3", blank=True, null=True)
    gre4 = models.GenericIPAddressField(protocol='IPv4', verbose_name="GRE4", blank=True, null=True)

class MikrotikLTE(NetworkDevice):
    pass

class Service(models.Model):
    SERVICE_TYPES = [
        ('internet', 'Интернет'),
        ('telephony', 'Телефония'),
    ]
    CONNECTION_TYPES = [
        ('wired', 'Проводной'),
        ('radio', 'Радио'),
        ('lte', 'LTE'),
    ]
    SPEED_CHOICES = [
        ('10M', '10 Mbit/s'),
        ('100M', '100 Mbit/s'),
        ('1G', '1 Gbit/s'),
        ('10G', '10 Gbit/s'),
    ]

    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES, verbose_name="Тип услуги")
    connection_type = models.CharField(max_length=50, choices=CONNECTION_TYPES, verbose_name="Способ подключения")
    speed = models.CharField(max_length=50, choices=SPEED_CHOICES, verbose_name="Скорость подключения")

    def __str__(self):
        return f"{self.get_service_type_display()} - {self.get_connection_type_display()} - {self.get_speed_display()}"

class DedicatedProvider(Service):
    gateway = models.ForeignKey(MikrotikGW, on_delete=models.CASCADE, verbose_name="Шлюз")

class ExternalIP(models.Model):
    dedicated_provider = models.OneToOneField(DedicatedProvider, on_delete=models.CASCADE, verbose_name="Выделенный провайдер")
    ip_address = models.GenericIPAddressField(protocol='IPv4', verbose_name="IP Адрес")
    mask = models.CharField(max_length=15, verbose_name="Маска")
    gw = models.GenericIPAddressField(protocol='IPv4', verbose_name="Шлюз")

class MobileProvider(Service):
    operator = models.CharField(max_length=255, verbose_name="Оператор")
    sim_card_number = models.CharField(max_length=20, verbose_name="Номер SIM-карты")

class Contract(models.Model):
    provider = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Провайдер")
    contract_number = models.CharField(max_length=255, verbose_name="Номер договора")
    contact_person = models.CharField(max_length=255, verbose_name="Контактное лицо")
    email = models.EmailField(verbose_name="Адрес электронной почты")

    def __str__(self):
        return self.contract_number