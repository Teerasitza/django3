from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello to thailand")

def about(request):
    return HttpResponse("เกี่ยวกับเรา")   

def contact(request):
    return HttpResponse("ติดต่อเรา")   