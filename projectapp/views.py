from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE

# Create your views here.
def index(request):
    return render(request,'projectapp/index.html')

def gejala(request):
    return render(request,'projectapp/gejala.html')

def daftarrsrujukan(request):
    return render(request,'projectapp/daftarrsrujukan.html')

def coba(request):
    return render(request,'projectapp/coba.html')

def external(request):
    inp = request.POST.get('param')
    out = run([sys.executable,'C:/Users/GANESHA/Documents/Aulia/django/project/test.py',inp],shell=False,stout=PIPE)
    print(out)

    return render(request,'projectapp/coba.html',{'data1':out})
