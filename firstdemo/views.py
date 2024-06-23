from  django.http import HttpResponse
from django.shortcuts import render
def aboutus(request):
    return HttpResponse( "wellcome to firstdemo")

def homepage(request):
    return render(request,"index.html")

def home(request):
    return HttpResponse("wellcome to home")


