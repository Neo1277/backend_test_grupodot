
from .models import Partner

from rest_framework.views import APIView
from rest_framework import status

from django.db.models import F

from django.http.response import JsonResponse

from .formulas_operations import QuotationOperationsAndFormulas

class LoanQuotation(APIView, QuotationOperationsAndFormulas):

    # Query (JOIN) que retorna los socios y el respectivo monto que presta cada uno
    def get_queryset(self):

        partners = Partner.objects.values(
            'id',
            'name',
            'partner_loan_capital__amount',
            'partner_loan_capital__interest_rate'
        ).annotate(
            partner_id=F('id'),
            partner_name=F('name'),
            loan_capital_amount=F('partner_loan_capital__amount'),
            loan_capital_interest_rate=F('partner_loan_capital__interest_rate'),
        )

        return partners

    def get(self, request, loanAmount):

        partners = self.get_queryset()

        partner_name = ''
        capital_amount = 0
        minor_interest_rate = 0

        # Iterar sobre los datos de la consulta para hallar el socio
        # cuyo prestamo se ajuste más a la solicitud con la tasa de
        # interés mas baja
        for partner in partners:

            if partner['loan_capital_amount'] >= loanAmount:

                if capital_amount == 0:

                    partner_name = partner['partner_name']
                    capital_amount = partner['loan_capital_amount']
                    minor_interest_rate = partner['loan_capital_interest_rate']
                else:

                    if (
                        partner['loan_capital_amount'] >= loanAmount and
                        partner['loan_capital_interest_rate'] < minor_interest_rate
                    ):
                        partner_name = partner['partner_name']
                        capital_amount = partner['loan_capital_amount']
                        minor_interest_rate = partner['loan_capital_interest_rate']

        # En caso de no hallar un valor que se ajuste al dinero solicitado mostrara el mensaje:
        # "No hay un socio disponible"
        if capital_amount == 0:

            message = "No hay socio disponible"

            return JsonResponse(
                {"message": message},
                safe=False,
                status=status.HTTP_400_BAD_REQUEST
            )

        interest_rate_percentage = self.get_interest_rate_percentage(minor_interest_rate)

        final_credit_total_payment = self.get_credit_total_payment(loanAmount, interest_rate_percentage)

        monthly_quota = self.get_monthly_quota(final_credit_total_payment)

        # Datos de salida, respuesta al request del endpoint
        outputData = {
            'Socio': partner_name,
            'Cuota_mensual': monthly_quota,
            'Pago_total_credito': final_credit_total_payment,
            'Tasa_interes_mensual': minor_interest_rate
        }

        return JsonResponse(outputData, safe=False, status=status.HTTP_200_OK)