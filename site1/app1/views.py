from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("xin chao cac ban")

def thaycuong(request):
    return HttpResponse("<h1><font color = green>CUONG CA DEP TRAI </font></h1>")
