from celery import shared_task
from .models import Contract

@shared_task
def log_new_contract(contract_id):
    contract = Contract.objects.get(id=contract_id)
    print(f"New contract added: {contract.contract_number}")
