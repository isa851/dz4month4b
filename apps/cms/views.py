from django.shortcuts import render
from apps.cms.models import Settings

# Create your views here.

def index(request):
    return render(request,"index.html",locals())