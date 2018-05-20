from django.shortcuts import render

# Create your views here.
from django.db import models
from django.shortcuts import render


# Create your models here.
def edit_page(request):
    return render(request, "editpages/edit.html")


def edit_page_bonus(request):
    return render(request, "editpages/materialize.html")

