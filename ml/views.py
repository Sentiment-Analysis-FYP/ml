from django.http import HttpResponse
from django.shortcuts import render
from .apps import WebAppConfig


def download(request):
    return HttpResponse('<h1>Download 1</h1>')


def test_connection(request):
    return HttpResponse('<h2>Request Received</h2>\n\n\n' + str(request.headers))
