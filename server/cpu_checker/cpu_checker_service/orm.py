from django.http import QueryDict

from .models import CpuData


def add_cpu_util_data(data: QueryDict) -> None:
    cpu_utilization = data.get("cpu_utilization")
    new_cpu_data = CpuData(cpu_utilization=cpu_utilization)
    new_cpu_data.save()
