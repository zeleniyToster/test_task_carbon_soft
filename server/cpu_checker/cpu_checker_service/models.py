from django.db import models


class CpuData(models.Model):
    cpu_utilization = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Утилизация ЦП, %')
