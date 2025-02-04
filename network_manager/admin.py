
from django.contrib import admin
from .models import Site, NetworkDevice, MikrotikGW, MikrotikLTE, Service, DedicatedProvider, ExternalIP, MobileProvider, Contract
#
# admin.site.register(Site)
# admin.site.register(NetworkDevice)
# admin.site.register(MikrotikGW)
# admin.site.register(MikrotikLTE)
# admin.site.register(Service)
admin.site.register(DedicatedProvider)
admin.site.register(ExternalIP)
admin.site.register(MobileProvider)
admin.site.register(Contract)




@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'td', 'legal_entity')  # Поля, отображаемые в списке
    list_filter = ('td', 'legal_entity')  # Фильтры справа
    search_fields = ('name', 'address')  # Поля для поиска



@admin.register(NetworkDevice)
class NetworkDeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'site', 'ip_address', 'login')
    list_filter = ('site',)
    search_fields = ('name', 'ip_address')



@admin.register(MikrotikGW)
class MikrotikGWAdmin(admin.ModelAdmin):
    list_display = ('name', 'site', 'ip_address', 'ext_ip', 'ext_gw')
    list_filter = ('site',)
    search_fields = ('name', 'ip_address', 'ext_ip')

from django.contrib import admin

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'connection_type', 'speed')
    list_filter = ('service_type', 'connection_type')
    search_fields = ('service_type', 'connection_type')