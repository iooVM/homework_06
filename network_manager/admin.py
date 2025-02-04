
from django.contrib import admin
from .models import Site, NetworkDevice, MikrotikGW, MikrotikLTE, Service, DedicatedProvider, ExternalIP, MobileProvider, Contract
#
# admin.site.register(Site)
# admin.site.register(NetworkDevice)
# admin.site.register(MikrotikGW)
# admin.site.register(MikrotikLTE)
# admin.site.register(Service)
# admin.site.register(DedicatedProvider)
# admin.site.register(ExternalIP)
# admin.site.register(MobileProvider)
# admin.site.register(Contract)




# @admin.register(Site)
# class SiteAdmin(admin.ModelAdmin):
#     list_display = ('name', 'address', 'td', 'legal_entity')  # Поля, отображаемые в списке
#     list_filter = ('td', 'legal_entity')  # Фильтры справа
#     search_fields = ('name', 'address')  # Поля для поиска



# @admin.register(NetworkDevice)
# class NetworkDeviceAdmin(admin.ModelAdmin):
#     list_display = ('name', 'site', 'ip_address', 'login')
#     list_filter = ('site',)
#     search_fields = ('name', 'ip_address')



# @admin.register(MikrotikGW)
# class MikrotikGWAdmin(admin.ModelAdmin):
#     list_display = ('name', 'site', 'ip_address', 'ext_ip', 'ext_gw')
#     list_filter = ('site',)
#     search_fields = ('name', 'ip_address', 'ext_ip')

# from django.contrib import admin
#
# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('service_type', 'connection_type', 'speed')
#     list_filter = ('service_type', 'connection_type')
#     search_fields = ('service_type', 'connection_type')


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('provider', 'contract_number', 'contact_person', 'email')
    list_filter = ('provider',)
    search_fields = ('contract_number', 'contact_person')

    @admin.action(description='Mark selected contracts as active')
    def mark_active(self, request, queryset):
        queryset.update(active=True)

# @admin.register(Contract)
# class ContractAdmin(admin.ModelAdmin):
#     list_display = ('provider', 'contract_number', 'contact_person', 'email')
#     list_filter = ('provider',)
#     search_fields = ('contract_number', 'contact_person', 'email')

# @admin.register(DedicatedProvider)
# class DedicatedProviderAdmin(admin.ModelAdmin):
#     list_display = ('service_type', 'connection_type', 'speed', 'gateway')
#     list_filter = ('service_type', 'connection_type')
#     search_fields = ('gateway__name', 'service_type')

@admin.register(ExternalIP)
class ExternalIPAdmin(admin.ModelAdmin):
    list_display = ('dedicated_provider', 'ip_address', 'mask', 'gw')
    list_filter = ('dedicated_provider',)
    search_fields = ('ip_address', 'dedicated_provider__provider')

@admin.register(MikrotikGW)
class MikrotikGWAdmin(admin.ModelAdmin):
    list_display = ('name', 'site', 'ip_address', 'ext_ip', 'ext_gw')
    list_filter = ('site',)
    search_fields = ('name', 'ip_address', 'ext_ip')

@admin.register(MikrotikLTE)
class MikrotikLTEAdmin(admin.ModelAdmin):
    list_display = ('name', 'site', 'ip_address')
    list_filter = ('site',)
    search_fields = ('name', 'ip_address')

@admin.register(MobileProvider)
class MobileProviderAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'connection_type', 'speed', 'operator', 'sim_card_number')
    list_filter = ('service_type', 'connection_type', 'operator')
    search_fields = ('operator', 'sim_card_number')

@admin.register(NetworkDevice)
class NetworkDeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'site', 'ip_address', 'login')
    list_filter = ('site',)
    search_fields = ('name', 'ip_address', 'login')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'connection_type', 'speed')
    list_filter = ('service_type', 'connection_type')
    search_fields = ('service_type', 'connection_type')

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'td', 'legal_entity')
    list_filter = ('td', 'legal_entity')
    search_fields = ('name', 'address', 'td')