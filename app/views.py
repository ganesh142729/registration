from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *

# Create your views here.

def registration(request):
    ERFO= Registrationform()
    d={'ERFO':ERFO}
    if request.method =='POST':
        DRFO =Registrationform(request.POST)
        if DRFO.is_valid():
            return HttpResponse(str(DRFO.cleaned_data))
    return render(request,'registration.html',d)