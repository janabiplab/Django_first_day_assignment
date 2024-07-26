from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the Website")
def basic_page(request):
    context={
        "message":"Welcome to the Website"
    }
    return render(request,"Main/basic_page.html",context)
