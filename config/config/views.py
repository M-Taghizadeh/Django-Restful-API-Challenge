from django.shortcuts import render
from requests import request


def index(request):
    return render(request=request, template_name='index.html', context={})