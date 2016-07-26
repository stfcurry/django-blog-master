from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Title,All
# Create your views here.
def test1(request):
    return HttpResponse("<h1>this is a test</h1>")

def test2(request):
    return render(request,"aa.html")

def index(request):
    title = Title.objects.all()
    all = All.objects.all()
    return render(request,"index.html",{"titles":title,"alls":all})

def body(request,name):
    title = Title.objects.all()
    all = All.objects.all
    body = All.objects.get(name=name)
    return render(request,"index.html",{"titles":title,"alls":all,"body":body})
