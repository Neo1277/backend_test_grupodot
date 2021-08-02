from django.urls import include, path, reverse

from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient

from .models import Partner, LoanCapital

import json

def create_partner(name):
    """
    Create a partner with the given parameters
    """

    return Partner.objects.create(name=name)

def create_loan_capital(loan_capital_data):
    """
    Create a Loan Capital with the given `loan_capital_data` dictionary
    """

    return LoanCapital.objects.create(**loan_capital_data)

class LoanQuotationTest(APITestCase, URLPatternsTestCase):

    urlpatterns = [
        path('', include('cotizacion_prestamo.urls')),
    ]

    def test_set_new_objects(self):
        """
        Ensure we can create a new object.
        """

        name = 'Juan'

        partner = create_partner(name)

        amount = 5000000
        interest_rate = 1.5

        loan_capital_data = {
            'amount': amount,
            'interest_rate':interest_rate,
            'partner_id': partner.id
        }

        loan_capital = create_loan_capital(loan_capital_data)

        client = APIClient()

        response = self.client.get('/loan_quotation/4000000')

        # Este request al endpoint cumplirá con lo solicitado y mostrará
        # el siguiente mensaje:
        self.assertEqual(json.loads(response.content), {
            'Socio': 'Juan',
            'Cuota_mensual': '171111.11',
            'Pago_total_credito': '6160000.00',
            'Tasa_interes_mensual': '1.50'
        })

        # Este request al endpoint no cumplirá con lo solicitado y mostrará
        # el siguiente mensaje:
        response = self.client.get('/loan_quotation/8000000')
        self.assertEqual(json.loads(response.content), {
            'message': 'No hay socio disponible'
        })
