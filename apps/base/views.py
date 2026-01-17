from django.shortcuts import render
from apps.base.models import Base
from apps.cms.models import Settings


# Create your views here.

def index(request):
    base = Base.objects.latest("id")
    settings = Settings.objects.latest("id")
    return render(request,"index.html",locals())