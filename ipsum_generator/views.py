from django.shortcuts import render
from .create_ipsum import create_text

# Create your views here.


def index(request):
    para1 = create_text(1)
    context = {"para1": para1}
    return render(request, "ipsum_generator/index.html", context=context)


def about(request):
    return render(request, "ipsum_generator/about.html")