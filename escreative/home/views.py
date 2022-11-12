from django.shortcuts import render
import os
from pathlib import Path


# list all slide show imgs name

def list_slide_show_imgs(path_to_slide_show_imgs="static\\imgs\\slide-show"):
    base_dir = os.getcwd()
    path_to_slide_show_imgs = os.path.join(base_dir, path_to_slide_show_imgs)

    slide_show_imgs = os.listdir(
        path_to_slide_show_imgs)
    return slide_show_imgs

# Create your views here.


def home(res):
    list_imgs = list_slide_show_imgs()
    len_slide_show_imgs = range(len(list_imgs)+1)
    return render(res, "home/home.html", {"slide_show_imgs": list_imgs, "len_slide_show_imgs": len_slide_show_imgs[1:]})


def kobutsusho(res):
    return render(res, "home/kobutsusho.html")
