from django.shortcuts import render
from apps.base.models import Base,Menu,Contact
from apps.cms.models import Settings


# Create your views here.

def index(request):
    base = Base.objects.latest("id")
    settings = Settings.objects.latest("id")
    return render(request,"index.html",locals())


def menu(request):
    menu = Menu.objects.all()
    return render(request, "menu-1-col.html", {"menu": menu})


def contact(request):
    contact = Contact.objects.last()
    return render(request, "contact-2.html", {"contact": contact})
