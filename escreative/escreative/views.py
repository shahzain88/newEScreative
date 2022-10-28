from django.shortcuts import render

def es404(res):
    return render(res,"404.html")