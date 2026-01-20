from django.shortcuts import render, redirect
from apps.base.models import Base, Menu, Contact, Contact_form
from apps.cms.models import Settings


def index(request):
    base = Base.objects.last()
    settings = Settings.objects.last()
    return render(request, "index.html", {"base": base,"settings": settings})


def menu(request):
    menu = Menu.objects.all()
    return render(request, "menu-1-col.html", {"menu": menu})


def contact(request):
    contact = Contact.objects.last()
    return render(request, "contact-2.html", {"contact": contact})


def contact_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact_form.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return redirect("contact_form") 

    return render(request, "contact-2.html")