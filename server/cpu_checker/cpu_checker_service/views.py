from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from cpu_checker_service.orm import add_cpu_util_data


def index(request: WSGIRequest) -> HttpResponse:
    return render(request, r"index.html")


def cpu_utilization_data_handler(request: WSGIRequest) -> None:
    cpu_util_data = request.POST
    add_cpu_util_data(cpu_util_data)
