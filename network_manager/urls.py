from django.urls import path
from . import views
from django.urls import path
from .views import (
    ContractListView, ContractDetailView, ContractCreateView,
    ContractUpdateView, ContractDeleteView
)

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('contracts/', views.contracts, name='contracts'),
    path('contract/<int:pk>/', views.contract_detail, name='contract_detail'),
    path('contract/add/', views.add_contract, name='add_contract'),
    path('contract/<int:pk>/edit/', views.edit_contract, name='edit_contract'),
    path('contract/<int:pk>/delete/', views.delete_contract, name='delete_contract'),

    path('dedicated-providers/', views.dedicated_providers, name='dedicated_providers'),
    path('external-ips/', views.external_ips, name='external_ips'),
    path('mikrotik-gws/', views.mikrotik_gws, name='mikrotik_gws'),
    path('mobile-providers/', views.mobile_providers, name='mobile_providers'),
    path('network-devices/', views.network_devices, name='network_devices'),
    path('services/', views.services, name='services'),
    path('sites/', views.sites, name='sites'),
]

# path('contract/<int:pk>/', ContractDetailView.as_view(), name='contract_detail'),
# path('contract/add/', ContractCreateView.as_view(), name='add_contract'),
# path('contract/<int:pk>/edit/', ContractUpdateView.as_view(), name='edit_contract'),
# path('contract/<int:pk>/delete/', ContractDeleteView.as_view(), name='delete_contract'),