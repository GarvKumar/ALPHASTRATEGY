from django.shortcuts import redirect, render
from django.conf import settings
# Create your views here.

def home(request):
    return render(request,"home.html")
def webdesign(request):
    return render(request, "webdesign.html")
def digitalmarketing(request):
    return render(request ,"dm.html")
def seo(request):
    return render(request,"seo.html")
def aboutus(request):
    return render(request,"aboutus.html")

