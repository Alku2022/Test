from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'index.html')

def high(request):
    return render(request,'high.html')


def low(request):
    return render(request,'low.html')


