from django.db import models
from crm.payment.models import Payment

class Report(models.Model):
    TOTAL_REPORT = [
        (1, 'Benefit'),
        (2, 'Damage'),
        (3, 'Did not Change ')
    ]

    reported_month = models.DateField()
    total_expense = models.BigIntegerField(null=True, blank=True, default=0)
    payment = models.ManyToManyField(Payment, related_name="payment")
    total_benefit_or_damage = models.IntegerField(choices=TOTAL_REPORT, default=3)
    money_left = models.BigIntegerField(null=True, blank=True, default=0)
    total_product = models.BigIntegerField(null=True, blank=True, default=0)
    left_product = models.BigIntegerField(null=True, blank=True, default=0)
    product_went_out = models.BigIntegerField(null=True, blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    generated_at = models.DateTimeField(auto_now_add=True)
    total_benefit = models.BigIntegerField(null=True, blank=True, default=0)
    def __str__(self):
        return self.reported_month

    def save(self, *args, **kwargs):
        # total_money = total_expense + money_left
        total_money = (self.total_expense or 0) + (self.money_left or 0)

        if self.total_benefit > total_money:
            self.total_benefit_or_damage = 1  # Benefit
        elif self.total_benefit < total_money:
            self.total_benefit_or_damage = 2  # Damage
        else:
            self.total_benefit_or_damage = 3  # Did not Change

        super().save(*args, **kwargs)