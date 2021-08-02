from django.db import models

# Source: Django documentation, Model field reference https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.DateTimeField

# Generate custom field for primary key
# https://docs.djangoproject.com/en/3.1/howto/custom-model-fields/#custom-database-types
# https://stackoverflow.com/a/56306262/9655579
class UnsignedAutoField(models.AutoField):
    def db_type(self, connection):
        return 'INT(10) UNSIGNED ZEROFILL AUTO_INCREMENT'

    def rel_db_type(self, connection):
        return 'INT(10) UNSIGNED ZEROFILL'

class Partner(models.Model):
    id = UnsignedAutoField(unique=True, primary_key=True)

    name = models.CharField(max_length=200)

    created_on = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the register was created"
    )

    updated_on = models.DateTimeField(
        auto_now=True,
        help_text="Date and time when the register was updated"
    )

class LoanCapital(models.Model):
    id = UnsignedAutoField(unique=True, primary_key=True)

    # Foreign key field
    partner = models.ForeignKey(
        Partner,
        on_delete=models.CASCADE,
        related_name='partner_loan_capital'
    )

    # interest rate
    amount = models.DecimalField(
        max_digits=11,
        decimal_places=2
    )

    # interest rate
    interest_rate = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the register was created"
    )

    updated_on = models.DateTimeField(
        auto_now=True,
        help_text="Date and time when the register was updated"
    )
