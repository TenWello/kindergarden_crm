# dashboard/models.py
from django.db import models

class DashboardConfig(models.Model):
    lookback_days = models.PositiveIntegerField(
        default=7,
        help_text="Grafikda necha kunni ko‘rsatish"
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Oxirgi {self.lookback_days} kun"
