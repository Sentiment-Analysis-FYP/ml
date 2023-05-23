from django.http import HttpResponse
from django.shortcuts import render
from .apps import WebAppConfig
from .download.download_json import send_file


def download(request, file_name):
    print(file_name)
    response = send_file(file_name)
    return response


def test_connection(request):
    return HttpResponse('<h2>Request Received</h2>\n\n\n' + str(request.headers))
