from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def HALAMAN1_views(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    #return HttpResponse(str("<h1>Hello World!</h1>"))
    return render (request, "home.html", {})

def KONTAK_views(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    return HttpResponse(str("<h1>HALAMAN KONTAK</h1>"))