# from django.test import TestCase
# from django.urls import reverse
# from .models import Contract

# class ContractModelTest(TestCase):
#     def setUp(self):
#         self.contract = Contract.objects.create(
#             provider="Provider A",
#             contract_number="12345",
#             contact_person="John Doe",
#             email="john@example.com"
#         )
#
#     def test_contract_creation(self):
#         self.assertEqual(self.contract.provider, "Provider A")
#         self.assertEqual(self.contract.contract_number, "12345")
#         self.assertEqual(self.contract.contact_person, "John Doe")
#         self.assertEqual(self.contract.email, "john@example.com")
#
#     def test_contract_update(self):
#         self.contract.provider = "Provider B"
#         self.contract.save()
#         updated_contract = Contract.objects.get(id=self.contract.id)
#         self.assertEqual(updated_contract.provider, "Provider B")
#
#     def test_contract_delete(self):
#         contract_id = self.contract.id
#         self.contract.delete()
#         with self.assertRaises(Contract.DoesNotExist):
#             Contract.objects.get(id=contract_id)


from django.test import TestCase
from .models import Contract, Service


class ContractModelTest(TestCase):
    def setUp(self):
        # Создаем экземпляр Service перед созданием контракта
        self.service = Service.objects.create(
            service_type='internet',
            connection_type='wired',
            speed='100M'
        )

        self.contract = Contract.objects.create(
            provider=self.service,  # Используем экземпляр Service
            contract_number="12345",
            contact_person="John Doe",
            email="john@example.com"
        )

    def test_contract_creation(self):
        self.assertEqual(self.contract.provider, self.service)  # Проверяем, что provider - это экземпляр Service
        self.assertEqual(self.contract.contract_number, "12345")
        self.assertEqual(self.contract.contact_person, "John Doe")
        self.assertEqual(self.contract.email, "john@example.com")

    def test_contract_update(self):
        self.contract.provider = self.service  # Обновляем provider
        self.contract.save()
        updated_contract = Contract.objects.get(id=self.contract.id)
        self.assertEqual(updated_contract.provider, self.service)

    def test_contract_delete(self):
        contract_id = self.contract.id
        self.contract.delete()
        with self.assertRaises(Contract.DoesNotExist):
            Contract.objects.get(id=contract_id)

class ContractViewsTest(TestCase):
    def setUp(self):
        self.contract = Contract.objects.create(
            provider="Provider A",
            contract_number="12345",
            contact_person="John Doe",
            email="john@example.com"
        )

    def test_contract_list_view(self):
        response = self.client.get(reverse('contracts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Provider A")

    def test_contract_detail_view(self):
        response = self.client.get(reverse('contract_detail', args=[self.contract.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "12345")

    def test_contract_create_view(self):
        response = self.client.post(reverse('add_contract'), {
            'provider': 'Provider B',
            'contract_number': '67890',
            'contact_person': 'Jane Doe',
            'email': 'jane@example.com'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Contract.objects.filter(contract_number="67890").exists())

    def test_contract_update_view(self):
        response = self.client.post(reverse('edit_contract', args=[self.contract.id]), {
            'provider': 'Provider C',
            'contract_number': '12345',
            'contact_person': 'John Doe',
            'email': 'john@example.com'
        })
        self.assertEqual(response.status_code, 302)
        updated_contract = Contract.objects.get(id=self.contract.id)
        self.assertEqual(updated_contract.provider, "Provider C")

    def test_contract_delete_view(self):
        response = self.client.post(reverse('delete_contract', args=[self.contract.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Contract.objects.filter(id=self.contract.id).exists())

