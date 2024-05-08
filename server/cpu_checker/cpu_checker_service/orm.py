from django.core import serializers
from django.http import QueryDict

from .models import CpuData


def add_cpu_util_data(data: QueryDict) -> None:
    cpu_utilization = data.get("cpu_utilization")
    new_cpu_data = CpuData(cpu_utilization=cpu_utilization)
    new_cpu_data.save()


def get_hundred_last_records():
    serialized_last_hundred_records = None
    try:
        serialized_last_hundred_records = serializers.serialize('json', CpuData.objects.all().order_by('-id')[:100],
                                                                fields=["cpu_utilization"])
    except Exception as ex:
        print(ex.args)
    return serialized_last_hundred_records
