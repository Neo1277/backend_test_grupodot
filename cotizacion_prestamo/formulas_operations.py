
# Clase para realizar calculos y formulas de la cotizacion
class QuotationOperationsAndFormulas(object):

    # Este método retorna el porcentaje de la tasa de interés de 0 a 1
    # Por ejemplo 1.50 = 0.015
    def get_interest_rate_percentage(self, minor_interest_rate):
        interest_rate_percentage = (minor_interest_rate * 1) / 100
        return interest_rate_percentage

    # Este método retorna el valor final a pagar teniendo en cuenta
    # La formula de interés simple: VF = VA (1 + n * i)
    def get_credit_total_payment(self, loanAmount, interest_rate_percentage):

        time_period = 36

        final_value = loanAmount * (1 + (time_period) * interest_rate_percentage)
        final_value = round(final_value, 2)

        return final_value

    # Este método retorna la cuota mensual a pagar
    def get_monthly_quota(self, final_credit_total_payment):

        monthly_quota = final_credit_total_payment/36
        monthly_quota = round(monthly_quota, 2)

        return monthly_quota