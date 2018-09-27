from django.shortcuts import render

def ola_mundo(request):
    return render(request, 'ola_mundo.html', {})

def segundapagina(request):
    return render(request, 'segundapagina.html', {})
# Create your views here.
