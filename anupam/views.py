from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Anupam

# Create your views here.

def index(request):
    items = Anupam.objects
    return render(request, 'anupam/index.html', {'items': items})

def details(request, anupam_id):
    item_detail = get_object_or_404(Anupam,pk=anupam_id)
    return render(request, 'anupam/detail.html',{'item':item_detail})
    