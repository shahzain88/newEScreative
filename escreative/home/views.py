from django.shortcuts import render

# Create your views here.
def home(res):
    return render(res, "home/home.html")

def kobutsusho(res):
    return render(res, "home/kobutsusho.html")