from django.urls import path
from . import views
from django.urls import path
from .views import (
    ContractListView, ContractDetailView, ContractCreateView,
    ContractUpdateView, ContractDeleteView, dedicated_providers_list,
    add_dedicated_provider, edit_dedicated_provider,
    external_ips_list, add_external_ip, edit_external_ip,
    mikrotik_gws_list, add_mikrotik_gw, edit_mikrotik_gw,
    mobile_providers_list, add_mobile_provider, edit_mobile_provider,
    network_device_list, add_network_device, edit_network_device,
    service_list, add_service, edit_service,
    site_list, add_site, edit_site,

)

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('contracts/', views.contracts, name='contracts'),
    path('contract/<int:pk>/', views.contract_detail, name='contract_detail'),
    path('contract/add/', views.add_contract, name='add_contract'),
    path('contract/<int:pk>/edit/', views.edit_contract, name='edit_contract'),
    path('contract/<int:pk>/delete/', views.delete_contract, name='delete_contract'),

    # path('dedicated-providers/', views.dedicated_providers, name='dedicated_providers'),
    # path('external-ips/', views.external_ips, name='external_ips'),
    # path('mikrotik-gws/', views.mikrotik_gws, name='mikrotik_gws'),
    # path('mobile-providers/', views.mobile_providers, name='mobile_providers'),
    # path('network-devices/', views.network_devices, name='network_devices'),
    # path('services/', views.services, name='services'),
    # path('sites/', views.sites, name='sites'),
    # path('dedicated-providers/', dedicated_providers_list, name='dedicated_providers_list'),
    # path('dedicated-provider/add/', add_dedicated_provider, name='add_dedicated_provider'),
    # path('dedicated-provider/edit/<int:id>/', edit_dedicated_provider, name='edit_dedicated_provider'),
    path('dedicated-providers/', dedicated_providers_list, name='dedicated_providers_list'),
    path('dedicated-provider/add/', add_dedicated_provider, name='add_dedicated_provider'),
    path('dedicated-provider/edit/<int:id>/', edit_dedicated_provider, name='edit_dedicated_provider'),

    # path('dedicated-providers/', dedicated_providers_list, name='dedicated_providers_list'),
    # path('dedicated-provider/add/', add_dedicated_provider, name='add_dedicated_provider'),
    # path('dedicated-provider/edit/<int:id>/', edit_dedicated_provider, name='edit_dedicated_provider'),
    path('external-ips/', external_ips_list, name='external_ips_list'),
    path('external-ip/add/', add_external_ip, name='add_external_ip'),
    path('external-ip/edit/<int:id>/', edit_external_ip, name='edit_external_ip'),
    path('mikrotik-gws/', mikrotik_gws_list, name='mikrotik_gws_list'),
    path('mikrotik-gw/add/', add_mikrotik_gw, name='add_mikrotik_gw'),
    path('mikrotik-gw/edit/<int:id>/', edit_mikrotik_gw, name='edit_mikrotik_gw'),
    path('mobile-providers/', mobile_providers_list, name='mobile_providers_list'),
    path('mobile-provider/add/', add_mobile_provider, name='add_mobile_provider'),
    path('mobile-provider/edit/<int:id>/', edit_mobile_provider, name='edit_mobile_provider'),
    path('network-devices/', network_device_list, name='network_device_list'),
    path('network-devices/add/', add_network_device, name='add_network_device'),
    path('network-devices/edit/<int:device_id>/', edit_network_device, name='edit_network_device'),
    path('services/', service_list, name='service_list'),
    path('services/add/', add_service, name='add_service'),
    path('services/edit/<int:service_id>/', edit_service, name='edit_service'),
    path('sites/', site_list, name='site_list'),
    path('sites/add/', add_site, name='add_site'),
    path('sites/edit/<int:site_id>/', edit_site, name='edit_site'),
]

# path('contract/<int:pk>/', ContractDetailView.as_view(), name='contract_detail'),
# path('contract/add/', ContractCreateView.as_view(), name='add_contract'),
# path('contract/<int:pk>/edit/', ContractUpdateView.as_view(), name='edit_contract'),
# path('contract/<int:pk>/delete/', ContractDeleteView.as_view(), name='delete_contract'),