from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("g2.")

def question(request):
    return HttpResponse("질문 목록")