from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from cpu_checker_service.orm import add_cpu_util_data, get_hundred_last_records


def index(request: WSGIRequest) -> HttpResponse:
    cpu_utilization_data = get_hundred_last_records()
    context = {
        'cpu_datas': cpu_utilization_data
    }
    return render(request, r"index.html", context)


@csrf_exempt
def cpu_utilization_data_handler(request: WSGIRequest):
    cpu_util_data = request.POST
    add_cpu_util_data(cpu_util_data)
    return HttpResponse()


def ajax_cpu_endpoint(request):
    cpu_utilization_data = get_hundred_last_records()
    return HttpResponse(cpu_utilization_data, content_type="application/json")
