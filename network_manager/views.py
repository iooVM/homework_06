
from django.shortcuts import render, get_object_or_404, redirect

from .models import Contract, DedicatedProvider, ExternalIP, MikrotikGW, MobileProvider, NetworkDevice, Service, Site

from .forms import ContractForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Contract


def contracts(request):
    contracts = Contract.objects.all()
    return render(request, 'network_manager/contracts.html', {'contracts': contracts})

def contract_detail(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    return render(request, 'network_manager/contract_detail.html', {'contract': contract})

def add_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    else:
        form = ContractForm()
    return render(request, 'network_manager/contract_form.html', {'form': form})

def edit_contract(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('contract_detail', pk=contract.pk)
    else:
        form = ContractForm(instance=contract)
    return render(request, 'network_manager/contract_form.html', {'form': form})

def delete_contract(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        contract.delete()
        return redirect('contracts')
    return render(request, 'network_manager/contract_confirm_delete.html', {'contract': contract})

def dedicated_providers(request):
    dedicated_providers = DedicatedProvider.objects.all()
    return render(request, 'network_manager/dedicated_providers.html', {'dedicated_providers': dedicated_providers})

def external_ips(request):
    external_ips = ExternalIP.objects.all()
    return render(request, 'network_manager/external_ips.html', {'external_ips': external_ips})

def mikrotik_gws(request):
    mikrotik_gws = MikrotikGW.objects.all()
    return render(request, 'network_manager/mikrotik_gws.html', {'mikrotik_gws': mikrotik_gws})

def mobile_providers(request):
    mobile_providers = MobileProvider.objects.all()
    return render(request, 'network_manager/mobile_providers.html', {'mobile_providers': mobile_providers})

def network_devices(request):
    network_devices = NetworkDevice.objects.all()
    return render(request, 'network_manager/network_devices.html', {'network_devices': network_devices})

def services(request):
    services = Service.objects.all()
    return render(request, 'network_manager/services.html', {'services': services})

def sites(request):
    sites = Site.objects.all()
    return render(request, 'network_manager/sites.html', {'sites': sites})

def home(request):
    return render(request, 'network_manager/home.html')


class ContractListView(ListView):
    model = Contract
    template_name = 'network_manager/contracts.html'
    context_object_name = 'contracts'

class ContractDetailView(DetailView):
    model = Contract
    template_name = 'network_manager/contract_detail.html'
    context_object_name = 'contract'

class ContractCreateView(CreateView):
    model = Contract
    form_class = ContractForm
    template_name = 'network_manager/contract_form.html'
    success_url = reverse_lazy('contracts')

class ContractUpdateView(UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = 'network_manager/contract_form.html'
    success_url = reverse_lazy('contracts')

class ContractDeleteView(DeleteView):
    model = Contract
    template_name = 'network_manager/contract_confirm_delete.html'
    success_url = reverse_lazy('contracts')
