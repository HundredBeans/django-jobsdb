from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Artikel, Lowongan
# Create your views here.
def beranda(request):
    artikel = Artikel.objects.all().order_by('-id')[0]
    lowongan = Lowongan.objects.all()
    info = {
        'flag':1,
        'lowongan':lowongan,
        'artikel':artikel,
    }
    return render(request, 'jobsdbApp/beranda.html', info)

def event(request):
    info = {
        'flag':3
    }
    return render(request, 'jobsdbApp/event.html', info)

def artikel(request, artikel_id):
    artikel = Artikel.objects.get(pk=artikel_id)
    articles = Artikel.objects.all().exclude(pk=artikel_id)
    info = {
        'artikel':artikel,
        'articles':articles
    }
    return render(request, 'jobsdbApp/artikel.html', info)

def resource(request):
    artikel = Artikel.objects.all()
    newest_artikel = Artikel.objects.all().order_by('-id')[0]
    info = {
        'artikel':artikel[1::-1],
        'newest_artikel':newest_artikel
    }
    return render(request, 'jobsdbApp/resource.html', info)

def searchResult(request):
    return render(request, 'jobsdbApp/search-result.html')
def detailLowongan(request):
    return render(request, 'jobsdbApp/detail-lowongan.html')