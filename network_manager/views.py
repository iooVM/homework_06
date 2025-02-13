
from django.shortcuts import render, get_object_or_404, redirect

from .models import Contract, DedicatedProvider, ExternalIP, MikrotikGW, MobileProvider, NetworkDevice, Service, Site

from .forms import ContractForm , DedicatedProviderForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ExternalIPForm
from .forms import MikrotikGWForm

from .forms import MobileProviderForm


from .forms import NetworkDeviceForm

from .forms import ServiceForm

from .forms import SiteForm



from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render




from django.contrib.auth.decorators import login_required


# def is_manager(user):
#     return user.groups.filter(name='managers').exists()
#
# def is_user(user):
#     return user.groups.filter(name='users').exists()

def is_manager(user):
    return user.groups.filter(name='managers').exists()

@user_passes_test(is_manager)
def manager_view(request):
    return render(request, 'manager_template.html')

def is_user(user):
    return user.groups.filter(name='users').exists()

@user_passes_test(is_user)
def user_view(request):
    return render(request, 'user_template.html')


@user_passes_test(is_manager)
def contracts(request):
    contracts = Contract.objects.all()
    return render(request, 'network_manager/contracts.html', {'contracts': contracts})


@user_passes_test(is_manager)
def contract_detail(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    return render(request, 'network_manager/contract_detail.html', {'contract': contract})

@user_passes_test(is_manager)
def add_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')
    else:
        form = ContractForm()
    return render(request, 'network_manager/contract_form.html', {'form': form})

@user_passes_test(is_manager)
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

@user_passes_test(is_manager)
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



def dedicated_providers_list(request):
    dedicated_providers = DedicatedProvider.objects.all()
    return render(request, 'network_manager/dedicated_providers_list.html', {'dedicated_providers': dedicated_providers})

# def add_dedicated_provider(request):
#     if request.method == 'POST':
#         # Логика для обработки формы добавления
#         pass
#     return render(request, 'add_dedicated_provider.html')
#
# def edit_dedicated_provider(request, id):
#     provider = get_object_or_404(DedicatedProvider, id=id)
#     if request.method == 'POST':
#         # Логика для обработки формы редактирования
#         pass
#     return render(request, 'edit_dedicated_provider.html', {'provider': provider})



def add_dedicated_provider(request):
    if request.method == 'POST':
        form = DedicatedProviderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dedicated_providers_list')
    else:
        form = DedicatedProviderForm()
    return render(request, 'network_manager/add_dedicated_provider.html', {'form': form})

def edit_dedicated_provider(request, id):
    provider = get_object_or_404(DedicatedProvider, id=id)
    if request.method == 'POST':
        form = DedicatedProviderForm(request.POST, instance=provider)
        if form.is_valid():
            form.save()
            return redirect('dedicated_providers_list')
    else:
        form = DedicatedProviderForm(instance=provider)
    return render(request, 'network_manager/edit_dedicated_provider.html', {'form': form})


@user_passes_test(is_user)

def external_ips_list(request):
    external_ips = ExternalIP.objects.all()
    return render(request, 'network_manager/external_ips_list.html', {'external_ips': external_ips})


@user_passes_test(is_user)

def add_external_ip(request):
    if request.method == 'POST':
        form = ExternalIPForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('external_ips_list')
    else:
        form = ExternalIPForm()
    return render(request, 'network_manager/add_external_ip.html', {'form': form})

@user_passes_test(is_user)

def edit_external_ip(request, id):
    external_ip = get_object_or_404(ExternalIP, id=id)
    if request.method == 'POST':
        form = ExternalIPForm(request.POST, instance=external_ip)
        if form.is_valid():
            form.save()
            return redirect('external_ips_list')
    else:
        form = ExternalIPForm(instance=external_ip)
    return render(request, 'network_manager/edit_external_ip.html', {'form': form})




def mikrotik_gws_list(request):
    mikrotik_gws = MikrotikGW.objects.all()
    return render(request, 'network_manager/mikrotik_gws_list.html', {'mikrotik_gws': mikrotik_gws})



def add_mikrotik_gw(request):
    if request.method == 'POST':
        form = MikrotikGWForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mikrotik_gws_list')
    else:
        form = MikrotikGWForm()
    return render(request, 'network_manager/add_mikrotik_gw.html', {'form': form})

def edit_mikrotik_gw(request, id):
    mikrotik_gw = get_object_or_404(MikrotikGW, id=id)
    if request.method == 'POST':
        form = MikrotikGWForm(request.POST, instance=mikrotik_gw)
        if form.is_valid():
            form.save()
            return redirect('mikrotik_gws_list')
    else:
        form = MikrotikGWForm(instance=mikrotik_gw)
    return render(request, 'network_manager/edit_mikrotik_gw.html', {'form': form})




def mobile_providers_list(request):
    mobile_providers = MobileProvider.objects.all()
    return render(request, 'network_manager/mobile_providers_list.html', {'mobile_providers': mobile_providers})



def add_mobile_provider(request):
    if request.method == 'POST':
        form = MobileProviderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mobile_providers_list')
    else:
        form = MobileProviderForm()
    return render(request, 'network_manager/add_mobile_provider.html', {'form': form})

def edit_mobile_provider(request, id):
    mobile_provider = get_object_or_404(MobileProvider, id=id)
    if request.method == 'POST':
        form = MobileProviderForm(request.POST, instance=mobile_provider)
        if form.is_valid():
            form.save()
            return redirect('mobile_providers_list')
    else:
        form = MobileProviderForm(instance=mobile_provider)
    return render(request, 'network_manager/edit_mobile_provider.html', {'form': form})



def network_device_list(request):
    network_devices = NetworkDevice.objects.all()
    return render(request, 'network_manager/network_device_list.html', {'network_devices': network_devices})




def add_network_device(request):
    if request.method == 'POST':
        form = NetworkDeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('network_device_list')  # Перенаправление на список устройств
    else:
        form = NetworkDeviceForm()
    return render(request, 'network_manager/add_network_device.html', {'form': form})

def edit_network_device(request, device_id):
    device = get_object_or_404(NetworkDevice, id=device_id)
    if request.method == 'POST':
        form = NetworkDeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return redirect('network_device_list')  # Перенаправление на список устройств
    else:
        form = NetworkDeviceForm(instance=device)
    return render(request, 'network_manager/edit_network_device.html', {'form': form})


def service_list(request):
    services = Service.objects.all()
    return render(request, 'network_manager/service_list.html', {'services': services})


def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')  # Перенаправление на список услуг
    else:
        form = ServiceForm()
    return render(request, 'network_manager/add_service.html', {'form': form})

def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')  # Перенаправление на список услуг
    else:
        form = ServiceForm(instance=service)
    return render(request, 'network_manager/edit_service.html', {'form': form})




def site_list(request):
    sites = Site.objects.all()  # Извлекаем все объекты Site
    return render(request, 'network_manager/site_list.html', {'sites': sites})  # Передаем их в шаблон


def add_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('site_list')  # Перенаправление на список сайтов
    else:
        form = SiteForm()
    return render(request, 'network_manager/add_site.html', {'form': form})

def edit_site(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('site_list')  # Перенаправление на список сайтов
    else:
        form = SiteForm(instance=site)
    return render(request, 'network_manager/edit_site.html', {'form': form})



class ContractListView(ListView):
    model = Contract
    template_name = 'network_manager/contracts.html'
    context_object_name = 'contracts'

class ContractDetailView(DetailView):
    model = Contract
    template_name = 'network_manager/contract_detail.html'
    context_object_name = 'contract'

# class ContractCreateView(CreateView):
#     model = Contract
#     form_class = ContractForm
#     template_name = 'network_manager/contract_form.html'
#     success_url = reverse_lazy('contracts')

from .tasks import log_new_contract

class ContractCreateView(CreateView):
    model = Contract
    form_class = ContractForm
    template_name = 'network_manager/contract_form.html'
    success_url = reverse_lazy('contracts')

    def form_valid(self, form):
        response = super().form_valid(form)
        log_new_contract.delay(self.object.id)  # Вызов фоновой задачи
        return response


class ContractUpdateView(UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = 'network_manager/contract_form.html'
    success_url = reverse_lazy('contracts')


class ContractDeleteView(DeleteView):
    model = Contract
    template_name = 'network_manager/contract_confirm_delete.html'
    success_url = reverse_lazy('contracts')

